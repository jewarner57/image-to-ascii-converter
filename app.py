from json_fix import fix_it

fix_it()
from flask import (
    redirect,
    render_template,
    url_for,
    request,
    flash,
    send_from_directory,
    current_app,
    send_file,
    jsonify,
)
from __init__ import app
from image_upload import uploadImage
from converter import (
    make_image_ascii_string,
    create_image_from_ascii_string,
    make_gif_ascii_string,
    create_gif_from_images,
)
import os
import json

# Error Handler Routes


@app.errorhandler(413)
def error413(e):
    return render_template("413.html"), 413


@app.errorhandler(404)
def error404(e):
    return render_template("404.html"), 404


# App Routes


@app.route("/")
def home():
    """Display the home page"""

    return render_template("home.html")


@app.route("/favicon.ico")
def favicon():
    """Sends the favicon to the client"""
    return send_from_directory(os.path.join(app.root_path, "static"), "./favicon.ico")


@app.route("/createGif", methods=["GET", "POST"])
def createGif():
    images = request.json.get("imageData")
    backgroundColor = request.json.get("backgroundColor")
    fontFamilyNumber = request.json.get("fontFamilyNumber")
    textColor = request.json.get("textColor")

    filename = create_gif_from_images(
        images, backgroundColor, fontFamilyNumber, textColor
    )

    return send_file(filename, mimetype="image/gif")


@app.route("/createImage", methods=["GET", "POST"])
def createImage():
    image = request.json.get("imageData")
    backgroundColor = request.json.get("backgroundColor")
    fontFamilyNumber = request.json.get("fontFamilyNumber")
    textColor = request.json.get("textColor")

    img = create_image_from_ascii_string(
        image, backgroundColor, fontFamilyNumber, textColor
    )

    filename = "./static/images/conversions/conversion.png"
    img.save(filename)

    return send_file(filename, mimetype="image/png")


@app.route("/convert", methods=["GET", "POST"])
def convert():
    """Display the converter page"""
    if request.method == "POST":

        # upload an image from the user
        image_info = uploadImage(request)
        image_filepath = image_info.get("filepath")
        image_extension = image_info.get("extension")

        # if the user uploaded a valid image
        if image_filepath is not None:

            char_key = request.form.get("charkey")

            image_width = int(request.form.get("image-width"))
            image_height = request.form.get("image-height")

            if char_key == "" or char_key == None:
                char_key = [".", ",", "*", "/", "(", "#", "%", "&", "@"]
            else:
                char_key = char_key.split(" ")

                # create the ascii art from the image
                if image_extension == "gif":
                    gif_ascii_data = make_gif_ascii_string(
                        image_filepath,
                        char_key,
                        image_width,
                        image_height,
                    )

                    ascii_art = gif_ascii_data.get("previewImage")
                    ascii_art_data = gif_ascii_data.get("frames")
                else:
                    ascii_art = make_image_ascii_string(
                        image_filepath,
                        char_key,
                        image_width,
                        image_height,
                    )
                    ascii_art_data = ascii_art

            # remove the image
            os.remove(image_filepath)

            # the ascii image string
            context = {
                "asciiImage": ascii_art,
                "imageData": json.dumps(ascii_art_data),
                "isAnimated": json.dumps(image_extension == "gif"),
            }

            return render_template("view.html", **context)
        else:
            flash("No Image Selected.")
            return redirect(url_for("convert"))

    else:

        context = {
            "uploadSize": int(current_app.config["MAX_CONTENT_LENGTH"] / 1024 / 1024)
        }

        return render_template("convert.html", **context)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

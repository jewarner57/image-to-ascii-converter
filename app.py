from flask import (
    redirect,
    render_template,
    url_for,
    request,
    flash,
    send_from_directory,
    current_app,
)
from __init__ import app
from image_upload import uploadImage, delete_file
from converter import make_image_ascii_string
import os

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


@app.route("/convert", methods=["GET", "POST"])
def convert():
    """Display the converter page"""
    if request.method == "POST":

        # upload an image from the user
        image_filepath = uploadImage(request)

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
            if image_height is not None:
                ascii_art = make_image_ascii_string(
                    image_filepath, char_key, int(image_width), int(image_height)
                )
            else:
                ascii_art = make_image_ascii_string(
                    image_filepath, char_key, int(image_width)
                )

            # remove the image
            os.remove(image_filepath)

            # the ascii image string
            context = {"asciiImage": ascii_art}

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
    app.run(debug=True)

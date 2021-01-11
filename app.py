from flask import redirect, render_template, url_for, request, flash
from __init__ import app
from image_upload import uploadImage, delete_file
from converter import make_image_ascii_string
import os

# App Routes


@app.route("/")
def home():
    """Display the home page"""

    return render_template("home.html")


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
            image_height = int(request.form.get("image-height"))

            if char_key == "" or char_key == None:
                char_key = [".", ",", "*", "/", "(", "#", "%", "&", "@"]
            else:
                char_key = char_key.split(" ")

            # create the ascii art from the image
            ascii_art = make_image_ascii_string(
                image_filepath, char_key, image_width, image_height
            )

            # remove the image
            os.remove(image_filepath)

            context = {"asciiImage": ascii_art}

            return render_template("view.html", **context)
        else:
            flash("No Image Selected.")
            return redirect(url_for("convert"))

    else:
        return render_template("convert.html")


if __name__ == "__main__":
    app.run(debug=True)

from __init__ import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from random import randint
from werkzeug.utils import secure_filename
import os


def uploadImage(request):
    """Saves the uploaded image"""
    if request.method == "POST":

        # check if the post request has the file part
        if "image" not in request.files:
            return None

        file = request.files["image"]

        if file.filename == "":
            return None

        fileType = allowed_file(file.filename)
        if not fileType:
            return None

        filename = get_unique_filename(secure_filename(file.filename))

        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # return the location of the image and its file type
        return {
            "filepath": os.path.join(UPLOAD_FOLDER, filename),
            "extension": fileType,
        }


def delete_file(filename):
    if filename != "default.jpg":
        os.remove(os.path.join(UPLOAD_FOLDER, filename))


def get_unique_filename(filename):
    # set the file name
    new_filename = filename

    # make a list of all filenames in the upload folder
    used_file_names = []
    for filename in os.listdir(UPLOAD_FOLDER):
        used_file_names.append(filename)

    # if the new filename is already used then randomize it
    randomized_filename = new_filename
    while randomized_filename in used_file_names:
        randomized_filename = f"{randint(100000, 999999)}_{new_filename}"

    new_filename = randomized_filename

    return new_filename


def allowed_file(filename):
    """Check if the file has an allowed extension"""
    extension = "." in filename and filename.rsplit(".", 1)[1].lower()

    if extension in ALLOWED_EXTENSIONS:
        return extension
    return False

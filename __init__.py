from flask import Flask
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# create flask app
app = Flask(__name__)

# configure secret key for app
app.secret_key = os.getenv("SECRET_KEY")

# set allowed upload extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# set image upload folder
UPLOAD_FOLDER = "./static/images/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# set max image upload size
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

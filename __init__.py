from flask import Flask
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# set allowed upload extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# set image upload folder
UPLOAD_FOLDER = "./static/images/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# set max image upload size
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

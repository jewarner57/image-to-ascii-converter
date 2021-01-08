from flask import Flask
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# create flask app
app = Flask(__name__)

# configure secret key for app
app.secret_key = os.getenv('SECRET_KEY')

from flask import redirect, render_template, url_for
from __init__ import app

# App Routes


@app.route('/')
def home():
    """Display the home page"""

    return render_template("home.html")


@app.route('/convert')
def convert():
    """Display the converter page"""

    return render_template("convert.html")


if __name__ == '__main__':
    app.run(debug=True)

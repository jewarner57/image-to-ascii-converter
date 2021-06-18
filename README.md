![Logo](./static/images/logo-image.png)
# Img To Ascii 
A web app for converting color images to beautiful ascii art with maximum freedom and customization.

---

## Why this project?
* Ascii converters are common on the internet, but many of them allow for minimal customization and use confusing or text heavy user interfaces.
  * This app provides an easy and highly customizeable ascii image conversion experience.
  * Change size, colors, fonts, character sets, and more with a UI designed specifically with ascii conversion in mind.

## Live project link
* Visit [imgtoascii.herokuapp.com](https://imgtoascii.herokuapp.com/) to try it out.

![Balloon Image in ASCII](./static/images/docs-images/readme-example.png)

---
## Index
* [Features](#Features)
* [How to run locally?](#Howtoinstallconfiglaunch)
* [Screenshots](#Screenshotsofapp)
* [Technologies used](#Technologiesused)

---

##  <a name='Features'></a>Features
  * Color image to conversion to ascii art
  * Easy to use UI custom designed for this project
  * Custom character sets for full control over the final product.
  * Full control over fonts, colors, and size
  * Conversion for image files up to 1 mb in online demo
    * You can increase the limit if you run the project locally

---

##  <a name='Howtoinstallconfiglaunch'></a>How to run locally?
1. clone the repository
2. navigate to the project's root directory 
3. install python dependencies from requirements.txt using: ```pip3 install -r ./requirements.txt```
4. run: ```python3 ./app.py```
5. Visit localhost:5000 in your browser

---

##  <a name='Screenshotsofapp'></a>Screenshots

![Flower Image in ASCII](./static/images/docs-images/readme-flower-example.gif)

![Mando Image in ASCII](./static/images/docs-images/starwars-docs-example.gif)

---

##  <a name='Technologiesused'></a>Technologies used
* Converter built with python
* Web application built with Flask and Jinja2
# Import modulst
from flask import Flask, render_template, request, render_template


# Establish flash
app = Flask(__name__)

# Scelton of the page

# Main index page
@app.route("/")
def home():
    return render_template(
        "home.html"
    )

# About page
@app.route("/about/")
def about():
    return render_template("about.html")


# Contact page
@app.route(("/contact/"))
def contact():
    return render_template("contact.html")



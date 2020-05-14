# Import modulst
from flask import Flask, render_template, request, render_template


# Establish flash
app = Flask(__name__)

# Scelton of the page

# Login page
@app.route("/")
def login():
    return render_template(
        "login.html"
    )

# Admin page
@app.route("/admin/")
def about():
    return render_template("admin.html")

# Changeps page
@app.route("/changeps/")
def changeps():
    # TODO
    return render_template("login.html")


# Changeps page
@app.route("/logout/")
def logout():
    # TODO
    return render_template("login.html")


# Changeps page
@app.route("/ledger/")
def ledger():
    # TODO
    return render_template("ledger.html")

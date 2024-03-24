from flask import Blueprint, render_template

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return render_template("index.html")


@contacts.route("/new", methods=['POST'])
def add_contact():
    return "Saving a contact"


@contacts.route("/update")
def update():
    return "Update a contact"


@contacts.route("/delete")
def delete():
    return "Delete a contact"


@contacts.route("/about")
def about():
    return render_template("about.html")

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/home.html")
def display_home():
    return render_template("home.html")

@app.route("/login.html")
def display_login():
    return render_template("login.html")

@app.route("/register.html")
def display_register():
    return render_template("register.html")

@app.route("/course1.html")
def display_courses():
    return render_template("courses.html")
from flask import Flask
from flask import render_template
from flask import request
import csv
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

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
    return render_template("courses.html", class_name=class_name)

@app.route("/classes.html")
def display_classes():
    return render_template("classes.html")

@app.route("/new_user.html", methods=["post"])#/new_user.html?email=a&username=d&password=12345678&student_prof=s
def register_new_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    student_prof = request.form['student_prof']
    add_user(username, email, password, student_prof)
    return render_template("home.html",user=username)

def read_users_csv():
    with open('database/users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

def add_user(username, email, password, student_prof):
    with open('database/users.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #Read last row and determine user_id or assign random userID
        user_id = random.randint(1000000, 9999999)
        writer.writerow([user_id, username, email, password, student_prof])
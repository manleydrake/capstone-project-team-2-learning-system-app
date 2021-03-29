from flask import Flask
from flask import render_template
from flask import request
import csv
import random
import hashlib

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

@app.route("/new_user.html", methods=["post"])
def register_new_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    student_prof = request.form['student_prof']
    add_user(username, email, hash_password(password), student_prof)
    return render_template("home.html",user=username)

@app.route("/login_user.html", methods=["post"])
def login_user():
    username = request.form['username']
    password = request.form['password']
    valid_log_in = is_login_valid(username, hash_password(password))
    if valid_log_in:
        return render_template("home.html", user=username)
    else:
        return render_template("login.html", error="invalid username or password")

def read_users_csv():
    with open('database/users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

def add_user(username, email, password, student_prof):
    with open('database/users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #Read last row and determine user_id or assign random userID
        user_id = random.randint(1000000, 9999999)
        writer.writerow([user_id, username, email, password, student_prof])

def is_login_valid(username, password):
    with open('database/users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        valid = False
        for row in reader:
            if(username in row and password in row):
                valid = True
        return valid

def hash_password(password):
    h = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
    return h.hex()
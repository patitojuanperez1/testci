from app import app
from flask import render_template, request
from models import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user is None: return "Unkown user"
        if not user.check_password(password): return "Wrong password"
        return "Hello " + user.username


        print("#################################")
        print(user)
        print("#################################")

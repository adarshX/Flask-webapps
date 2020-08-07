from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello ady"

@app.route("/members")
def members():
    a = "Adarsh" + "\n" + "Sid"+  '\n' + "Reethu"
    return a
@app.route("/layout")
def lay():
    return render_template("layout.html")


if __name__== "__main__":
    app.run()

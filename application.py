from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/p1")
def p1():
    return render_template("p1.html")
    
@app.route("/p2")
def p2():
    return render_template("p2.html")   
    
from flask import render_template
from . import main 



@main.route('/')
def homepage():
    return render_template("homepage.html")
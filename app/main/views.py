from flask import render_template
from . import main 


# Homepage view 
@main.route('/')
def homepage():
    return render_template("homepage.html")


# Projects view page 
@main.route('/projects')
def projects():
    return render_template('projects.html')


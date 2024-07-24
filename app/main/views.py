from flask import render_template
from . import main 
from ..models import Project

# Homepage view 
@main.route('/')
def homepage():
    return render_template("homepage.html")


# Projects view page 
@main.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)


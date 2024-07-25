from flask import render_template, redirect, url_for, flash , request
from flask_login import login_required 
from ..models import Project 
from slugify import slugify 
from . import admin 



@admin.route('/admin/dashboard')
def dashboard():
    projects = Project.query.all()
    return render_template('admin/dashboard.html', projects=projects)



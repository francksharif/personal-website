from flask import render_template
from ..models import Project
from . import project


@project.route('/project/<slug>')
def project(slug):
    project = Project.query.filter_by(slug=slug).first()
    return render_template('project/project.html', project=project)
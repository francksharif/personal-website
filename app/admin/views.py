import os
from . import admin
from .. import db
from flask import current_app, render_template, redirect, url_for, flash , request
from flask_login import login_required 
from ..models import Project 
from slugify import slugify 
from werkzeug.utils import secure_filename
from sqlalchemy import exc



@admin.route('/admin/dashboard')
def dashboard():
    projects = Project.query.all()
    return render_template('admin/dashboard.html', projects=projects)


@admin.route('/admin/project/create', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        title = request.form.get('title')
        small_description = request.form.get('small-description')
        description = request.form.get('description')
        github_link = request.form.get('github-link')
        project_link = request.form.get('project-link')
        slug = slugify(title)

        # Handle image uploading
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)


        project = Project(
            title=title,
            small_description=small_description,
            description=description,
            image_file=filename,
            github_link=github_link,
            project_link=project_link,
            slug=slug
        )
        
        try:
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('admin.dashboard'))
        except exc:
            db.session.rollback()
     
        flash('Project published!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/new_project.html')



@admin.route('/admin/project/edit/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.small_description = request.form['small-description']
        project.description = request.form['description']
        project.github_link = request.form['github-link']
        project.project_link = request.form.get('project-link', '')

        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                filename = secure_filename(file.filename)
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                project.image_file = filename

        db.session.commit()
        flash('Project updated successfully!')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/edit_project.html', project=project)



@admin.route('/admin/project/delete/<int:id>', methods=['GET', 'POST'])
def delete_project(id):
    project = Project.query.get_or_404(id)
    if request.method=='POST':
        if request.form.get('response') == 'Yes':
            db.session.delete(project)
            db.session.commit()
            flash('Project deleted successfully', 'success')
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/delete_project.html', project=project)

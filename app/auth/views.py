from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user, login_required 
from ..models import Admin
from . import auth




auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin.dashboard'))
        flash('INVALID CREDENTIALS', 'danger')
    return render_template('auth/login.html')




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
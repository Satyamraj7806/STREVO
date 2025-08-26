from flask import Flask, render_template, Blueprint, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm
from .models import User
from app import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home_page():
    return render_template('home.html')
@main.route('/videos')
def videos_page():
    return render_template('videos.html')

@main.route('/music')
def music_page():
    return render_template('music.html')

@main.route('/minis')
def minis_page():
    return render_template('minis.html')
@main.route('/community')
def community_page():
    return render_template('community.html')
@main.route('/profile')
def profile_page():
    return render_template('profile.html')

@main.route('/settings')
def settings_page():
    return render_template('settings.html')

@main.route('/about')
def about_page():
    return render_template('about.html')

@main.route('/contact')
def contact_page():
    return render_template('contact.html')

@main.route('/login', methods=['GET', 'POST'])
@main.route('/register', methods=['GET', 'POST'])
def register_page():
    view = request.args.get('view', 'register')
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_to_create = User(
            username = register_form.username.data,
            email_id = register_form.email_id.data,
            password = register_form.password1.data    
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully!! You are logged in as {user_to_create.username}", category= 'success')
        return redirect (url_for('main.home_page'))
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(username =login_form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password = login_form.password1.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category='success')
            return redirect(url_for('main.home_page'))
        else :
            flash(f'Username and password do not match! Please try again.', category='danger')

   
    return render_template('register.html', login_form = login_form, register_form = register_form, view = view)

@main.route('/logout')
def logout_page():
    logout_user()
    flash(f' You have been logged out !', category = 'info')
    return redirect (url_for('main.home_page'))




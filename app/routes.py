#!/usr/bin/python3
"""all my routes"""

from flask import Flask, render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import SigninForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
import os
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """Home page Route"""
    title = 'Implicit Declarations'  # Title to be passed to the template
    
    return render_template('index.html', title=title)

@app.route('/blog')  # Define the 'blog' endpoint
def blog():
    # Add your blog logic here
   
    return render_template('blog.html')

@app.route('/about') 
def about():
    # Add your blog logic here
    return render_template('about.html')

@app.route('/services')  
def services():
    # Add your blog logic here
    return render_template('services.html')

@app.route('/contact')  
def contact():
    # Add your blog logic here
    return render_template('contact.html')





@app.route('/post/<int:post_id>')
def single_post(post_id):
    # Add your blog logic here
    # post = something
    return render_template('post.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Sign in view function logic"""
    # Check if the user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # Create an instance for the login form
    form = SigninForm()

    # check if the form has been submitted is valid
    if form.validate_on_submit():
        # look up the user in db by their username
        user = User.query.filter_by(username=form.username.data).first()

        # Check if the user doesn't exist or if password is incorrect
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        
        # Login the user and remember their choice to stay logged in
        login_user(user, remember=form.remember_me.data)

        # Check if there's a next parameter in the URL & redirect to that page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    # Render the login form template when visited    
    return render_template('signin.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    """Logout view function"""
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User sign up form"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/user/<username>')
@login_required
def profile(username):
    """Profile Page"""
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user, posts=posts)


def save_image(picture_file):
    picture_name = picture_file.filename
    picture_path = os.path.join(app.root_path, 'static/profile_pics' ,picture_name)
    picture_file.save(picture_path)
    return picture_name


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()    
    if form.validate_on_submit():
        image_file = save_image(form.picture.data)
        current_user.image_file = image_file
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        image_url = None  # Initialize to None
        if current_user.image_file:    
            image_url = url_for('static', filename='profile_pics/' + current_user.image_file)    
    return render_template('edit_profile.html', title='Edit Profile', form=form, image_url=image_url)



@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)


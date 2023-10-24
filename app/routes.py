#!/usr/bin/python3
"""all my routes"""

from flask import Flask, render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import SigninForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# @app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """Home page Route"""
    title = 'Implicit Declarations'  # Title to be passed to the template
    user = current_user
    return render_template('index.html', title=title, user=user)

@app.route('/blog')  # Define the 'blog' endpoint
def blog():
    # Add your blog logic here
    user = current_user
    return render_template('blog.html', user=user)

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

@app.route('/contact')
@login_required  
def dashboard():
    # Add your blog logic here
    return render_template('dashboard.html')



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
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user, posts=posts)
   

if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/python3
"""all my routes"""

from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory,abort
from app import app, db
from app.forms import SigninForm, RegistrationForm, EditProfileForm, EmptyForm, AddPostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from werkzeug.urls import url_parse
import os
from datetime import datetime
import imghdr
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """Home page Route"""
    title = 'Implicit Declarations' 
    posts = Post.query.all()
    #files = os.listdir(app.config['UPLOAD_PATH'])
    
    return render_template('index.html', title=title, posts=posts)

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
    posts = user.posts        
    form = EmptyForm()
    return render_template('profile.html', user=user, posts=posts,
                            form=form)




@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)     
    if form.validate_on_submit():        
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.picture = form.picture.data

        # Check if an image was uploaded
        if form.picture.data:
            uploaded_file = form.picture.data
            filename = secure_filename(uploaded_file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                        file_ext != validate_image(uploaded_file.stream):
                    flash('Invalid image format. Please upload a valid image (jpg, png, gif).', 'error')
                    return redirect(url_for('edit_profile'))
                
                # Save the image to the server
                image_path = os.path.join(app.config['UPLOAD_PATH'], filename)
                uploaded_file.save(image_path)

                # Store the image filename in the database
                current_user.picture = filename
                 
                
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.picture.data = current_user.picture
        
    return render_template('edit_profile.html', title='Edit Profile', form=form)



@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))

"""NEW CODE GOES HERE"""

def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = AddPostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, title=form.title.data, author=current_user)

        # Check if an image was uploaded
        if form.image.data:
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                        file_ext != validate_image(uploaded_file.stream):
                    flash('Invalid image format. Please upload a valid image (jpg, png, gif).', 'error')
                    return redirect(url_for('add_post'))

                # Save the image to the server
                image_path = os.path.join(app.config['UPLOAD_PATH'], filename)
                uploaded_file.save(image_path)

                # Store the image filename in the database
                post.image = filename                

        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    return render_template('add_post.html', title='Add post', form=form)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(debug=True)


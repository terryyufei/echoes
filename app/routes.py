#!/usr/bin/python3
"""all my routes"""

from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
from app import app, db
from app.forms import SigninForm, RegistrationForm, EditProfileForm, EmptyForm, AddPostForm, ResetPasswordForm, ResetPasswordRequestForm
from app.forms import EditPostForm, DeleteConfirmationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post, Category
from werkzeug.urls import url_parse
import os
from datetime import datetime
import imghdr
from werkzeug.utils import secure_filename
from app.email import send_password_reset_email


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """Landing page Route"""
    title = 'Echoes'     
    return render_template('index.html')

@app.route('/blog', methods=['GET', 'POST'])  
def blog():  
    # Pagination
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    
    # Next and previous page links.
    next_url = url_for('blog', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('blog', page=posts.prev_num) \
        if posts.has_prev else None
    
    authors = [post.author for post in posts]
    
    return render_template('blog.html', posts=posts.items, authors=authors, title='Blog',
                           next_url=next_url, prev_url=prev_url)




 
@app.route('/post/<int:post_id>')
def single_post(post_id):
   post = Post.query.get_or_404(post_id)
   author = post.author
   return render_template('single_post.html', post=post, author=author)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Sign in view function logic"""
    # Check if the user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    
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
            next_page = url_for('blog')
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
        return redirect(url_for('blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/user/<username>') #user
@login_required
def user(username):
    """Profile Page"""   
    user = User.query.filter_by(username=username).first_or_404()    
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    authors = [post.author for post in posts]      
    form = EmptyForm() # followers
    return render_template('user.html', user=user, posts=posts.items, authors=authors,
                            next_url=next_url, prev_url=prev_url, form=form)




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
            return redirect(url_for('blog'))
        if user == current_user:
            flash('You cannot follow yourself!')
            return redirect(url_for('blog', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are now following {}!'.format(username))
        return redirect(url_for('blog', username=username))
    else:
        return redirect(url_for('blog'))

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
            return redirect(url_for('blog', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You unfollowed {}.'.format(username))
        return redirect(url_for('blog', username=username))
    else:
        return redirect(url_for('blog'))

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

        # Get the selected category from the form
        category_id = form.category.data
        category = Category.query.get(category_id)
        post.category = category

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
        return redirect(url_for('blog'))

    return render_template('add_post.html', title='Add post', form=form)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    """Reset password request"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('signin'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)
    
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Password reset view function"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('signin'))
    return render_template('reset_password.html', form=form)


@app.route('/category/<category_name>')
def category(category_name):
    """Filter using categories"""
    # Retrieve posts in the specified category from database
    category_posts = Post.query.filter(Post.category.has(name=category_name)).all()
    authors = [post.author for post in category_posts]   
    return render_template('category.html', category_name=category_name, category_posts=category_posts, authors=authors)

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    """Edit post""" 
    post = Post.query.get_or_404(post_id)
    form = EditPostForm(obj=post)
    if form.validate_on_submit():
        # Update post attributes with form data
        post.title = form.title.data
        post.content = form.content.data

        # Ensure that 'category' is set with the ID of the selected category
        category_id = form.category.data
        category = Category.query.get(category_id)
        post.category = category
        db.session.commit()
        flash('Post updated successfully')
        return redirect(url_for('blog', post_id=post.id))
    return render_template('edit_post.html', post=post, form=form)

@app.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    """Delete a post view function"""
    post = Post.query.get_or_404(post_id)
    form = DeleteConfirmationForm(obj=post)
    if form.validate_on_submit():
        if request.method == 'POST':
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted successfully')
            return redirect(url_for('blog'))
    return render_template('delete_post.html', post=post, form=form)



    

if __name__ == '__main__':
    app.run(debug=True)


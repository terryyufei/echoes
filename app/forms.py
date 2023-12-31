"""Sign in, Sign up forms"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import User, Category
from flask_ckeditor import CKEditorField




class SigninForm(FlaskForm):
    """signing in form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """User registartion form"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), Regexp(
        r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])', message="Password must include at least one uppercase letter, one lowercase letter, and one digit.")
    ])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Update Username')
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    picture = FileField(label="Upload Profile Picture", validators=[
                        FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Update Profile')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
    """for following & unfollowing"""
    submit = SubmitField('Submit')


class AddPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={
                        "placeholder": "Title"})
    category = SelectField('Category', choices=[
        ('', 'Category'),
        ('1', 'General'),
        ('2', 'Tech'),
        ('3', 'Animals'),
        ('4', 'Comedy'),
        ('5', 'Mystrey'),
        ('6', 'Culture'),
        ('6', 'Travel'),
        ('6', 'People')
    ], validators=[DataRequired()])
    #content = TextAreaField('Tell your story', validators=[DataRequired()], render_kw={"placeholder": "Tell your story"})
    content = CKEditorField('Content', validators=[DataRequired()], render_kw={"placeholder": "Tell your story"})
    is_featured = BooleanField('Featured')
    image = FileField(label="Upload Post Picture", validators=[
                      FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Publish')


class ResetPasswordRequestForm(FlaskForm):
    """Request password request form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    """password reset form"""
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class EditPostForm(FlaskForm):
    """Edit post form"""
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    image = FileField(label="Upload Post Picture", validators=[
                      FileAllowed(['jpg', 'png']), FileRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save changes')
    
    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        # Populate the category choices dynamically from the database
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]


class DeleteConfirmationForm(FlaskForm):
    """Deleting post"""
    confirm = SubmitField('Delete')
    submit = SubmitField('Delete Post')





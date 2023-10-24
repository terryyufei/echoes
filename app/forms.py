"""Sign in, Sign up forms"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models import User


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
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])    
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
    picture = FileField(label="Upload Profile Picture", validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Update Profile')

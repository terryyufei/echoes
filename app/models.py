"""Database Models"""

from app import db, login
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5



class User(UserMixin, db.Model):
    """User database model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(3))
    image_file = db.Column(db.String(120), nullable=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """specifies how to print objects of this class"""
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        """Password hashing"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Password verification"""
        return check_password_hash(self.password_hash, password)
    
    
    
   
            


class Post(db.Model):
    """Posts database Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    image = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    """Flask-Login user load function"""
    return User.query.get(int(id))

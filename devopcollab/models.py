from devopcollab import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin=db.Column(db.Boolean(), nullable=False)
    # This connects BlogPosts to a User Author.
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.is_admin=False

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"UserName: {self.username} --- Is_Admin: {self.is_admin} --- ID: {self.id}"

class BlogPost(db.Model):
    # Setup the relationship to the User table
    users = db.relationship(User)

    # Model for the Blog Posts on Website
    id = db.Column(db.Integer, primary_key=True)
    # Notice how we connect the BlogPost to a particular author
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    status = db.Column(db.String(20),nullable=False, default='Open')
    text = db.Column(db.Text, nullable=False)
    effort_hour=db.Column(db.Integer, nullable=True)
    devops_onwer=db.Column(db.String(100), nullable=False)

    def __init__(self, title, text, user_id, status, effort_hour=0, devops_owner='devops'):
        self.title = title
        self.text = text
        self.user_id =user_id
        self.status=status
        self.effort_hour=effort_hour
        self.devops_onwer=devops_owner


    def __repr__(self):
        return f"Post Id: {self.id} --- Date: {self.date} --- Title: {self.title} --- Author: {self.user_id} --- Status: {self.status} --- Effort_Hour: {self.effort_hour} --- DevOps_Onwer: {self.devops_onwer}"

    # def to_dict(self):
    #     return {
    #         'title': self.title,
    #         'text': self.text,
    #     }

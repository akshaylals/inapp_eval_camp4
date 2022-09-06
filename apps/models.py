from flask_login import UserMixin
import datetime
from .database import db

class Users(db.Model, UserMixin):
    id          = db.Column(db.Integer, primary_key=True)
    firstName   = db.Column(db.String(20), nullable=False)
    lastName    = db.Column(db.String(20), nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(300), nullable=False)

    blogs       = db.relationship('Blogs')
    comments    = db.relationship('Comments')

    def __init__(self, firstName, lastName, password, email) -> None:
        self.firstName  = firstName
        self.lastName   = lastName
        self.password   = password
        self.email      = email


class Blogs(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(50), nullable=False)
    content     = db.Column(db.String(1000), nullable=False)
    dt          = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    author      = db.Column(db.Integer, db.ForeignKey("users.id"))

    comments    = db.relationship('Comments')

    def __init__(self, title, content, author) -> None:
        self.title   = title
        self.content = content
        self.author  = author


class Comments(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    comment     = db.Column(db.String(100), nullable=False)
    dt          = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user        = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog        = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def __init__(self, comment, user, blog) -> None:
        self.comment = comment
        self.user    = user
        self.blog    = blog
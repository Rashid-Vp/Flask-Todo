from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    username = db.Column(db.String(150))

class Todo(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user = db.Column(db.String(150))
    text = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
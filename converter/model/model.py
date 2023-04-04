from flask_sqlalchemy import SQLAlchemy
from enum import Enum
import datetime

db = SQLAlchemy()

class Status(Enum):
    UPLOADED = 'UPLOADED'
    PROCESSED = 'PROCESSED'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(128))
    new_format = db.Column(db.String(10))
    status = db.Column(db.Enum(Status), default=Status.UPLOADED)
    time_stamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return "file_name: {} - new_format: {} - status: {} - time_stamp: {}".format(self.file_name, self.new_format, self.status.value, self.time_stamp)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    tasks = db.relationship('Task', cascade='all, delete, delete-orphan')

    def __repr__(self) -> str:
        return "user_name: {} - email: {} - password: {}".format(self.user_name, self.email, self.password)
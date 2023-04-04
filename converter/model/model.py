from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from enum import Enum
import datetime

db = SQLAlchemy()

class Status(Enum):
    UPLOADED = 0
    PROCESSED = 1

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(128))
    new_format = db.Column(db.String(10))
    status = db.Column(db.Enum(Status), nullable=False, default=Status.UPLOADED)
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
    
class EnumToDictionary(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'value': value.value}
    
class TaskSchema(SQLAlchemyAutoSchema):
    status = EnumToDictionary(attribute=('status'))
    class Meta:
        model = Task
        include_relationships = True
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
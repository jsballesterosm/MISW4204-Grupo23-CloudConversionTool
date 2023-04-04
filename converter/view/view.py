from flask_restful import Resource
from ..model import db, User, UserSchema, Task, TaskSchema, UserSignupSchema
from flask import request
from marshmallow import ValidationError

user_schema = UserSchema()
task_schema = TaskSchema()
signup_schema = UserSignupSchema()

class Signup(Resource):
    def post(self):
        try:
            # Obtenemos el request body y lo deserializamos con Marshmallow
            data = signup_schema.load(request.json)
            
            # Verificamos si ya existe un usuario con el mismo username o email
            if User.query.filter_by(username=data['username']).first():
                return {"message": "Username already exists"}, 409
            elif User.query.filter_by(email=data['email']).first():
                return {"message": "Email already exists"}, 409
            
            # Verificamos que las contraseñas coincidan
            if data['password1'] != data['password2']:
                return {"message": "Passwords don't match"}, 400
            
            # Creamos el usuario a partir de los datos obtenidos
            user = User(
                username=data['username'],
                email=data['email'],
                password=data['password1']
            )
            
            # Si todo está bien, creamos el usuario y lo guardamos en la base de datos
            db.session.add(user)
            db.session.commit()
            return {"message": "User created successfully"}, 200
        except ValidationError as e:
            return {"message": e.messages}, 400

class UserList(Resource):
    def get(self):
        return [user_schema.dump(user) for user in User.query.all()]

class TaskList(Resource):
    def get(self):
        return [task_schema.dump(task) for task in Task.query.all()]
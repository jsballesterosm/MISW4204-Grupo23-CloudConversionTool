from converter import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .view import UserList, TaskList, Signup, Login
from .model import db, UserSchema, TaskSchema, User, Task

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(UserList, '/api/users')
api.add_resource(TaskList, '/api/tasks')
api.add_resource(Signup, '/api/auth/signup')
api.add_resource(Login, '/api/auth/login')

jwt = JWTManager(app)

with app.app_context():
    user_schema = UserSchema()
    task_schema = TaskSchema()
    u = User(username='admin', email='admin@uniandes.edu.co', password='adminadmin')
    t1 = Task(fileName='sample.zip', newFormat='7z')
    t2 = Task(fileName='sample.7z', newFormat='zip')
    u2 = User(username='d.leyvad', email='d.leyvad@uniandes.edu.co', password='12345678')
    t3 = Task(fileName='sample.zip', newFormat='7z')
    t4 = Task(fileName='sample.7z', newFormat='zip')
    u.tasks.append(t1)
    u.tasks.append(t2)
    u2.tasks.append(t3)
    u2.tasks.append(t4)
    db.session.add(u)
    db.session.add(u2)
    db.session.commit()
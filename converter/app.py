from converter import create_app
from .model import db, User, Task
from .model import UserSchema, TaskSchema
from flask_restful import Api
from .view import UserList, TaskList, Signup

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(UserList, '/api/users')
api.add_resource(TaskList, '/api/tasks')
api.add_resource(Signup, '/api/auth/signup')

# Flask library
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Models
from models import db

# Views
from view import (
    UserListView, 
    TaskListView, 
    SignupView, 
    LoginView, 
    TaskView, 
    FileView,
    ProcessView
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SN4kRspz%7#cb^;u@10.32.80.3/cloud_conversion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'platipus'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(UserListView, '/api/users')
api.add_resource(TaskListView, '/api/tasks')
api.add_resource(TaskView, '/api/tasks/<int:id_task>')
api.add_resource(SignupView, '/api/auth/signup')
api.add_resource(LoginView, '/api/auth/login')
api.add_resource(FileView, '/api/files/<string:filename>')
api.add_resource(ProcessView, '/process')

import logging
from logging.handlers import RotatingFileHandler

file_handler = RotatingFileHandler('logs/myapp.log', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)

jwt = JWTManager(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
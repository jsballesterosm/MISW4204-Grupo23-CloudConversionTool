# flask library
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# models
from models import db

# views
from view import (
    UserListView, 
    TaskListView, 
    SignupView, 
    LoginView, 
    TaskView, 
    FileView
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@172.31.39.69:5432/cloud_conversion'
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

jwt = JWTManager(app)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
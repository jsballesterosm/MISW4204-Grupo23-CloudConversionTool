from converter import create_app
from .model import db, User, Task
from .model import UserSchema, TaskSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    user_schema = UserSchema()
    task_schema = TaskSchema()
    u = User(user_name='Felipe', email='d.leyvad@uniandes.edu.co', password='admin')
    t1 = Task(file_name='sample.zip', new_format='7z')
    t2 = Task(file_name='sample.7z', new_format='zip')
    u.tasks.append(t1)
    u.tasks.append(t2)
    db.session.add(u)
    db.session.commit()
    print([user_schema.dumps(user) for user in User.query.all()])
    print([task_schema.dumps(task) for task in Task.query.all()])

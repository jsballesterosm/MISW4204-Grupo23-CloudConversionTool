# Libraries
from marshmallow import ValidationError
from google.cloud import storage

# Flask Libraries
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request, send_file

# Utilities
from tasks import compress_file
from datetime import (
    datetime,
    timedelta
)
import os

# Models
from models import (
    db, 
    User, 
    UserSchema, 
    Task, 
    TaskSchema, 
    UserSignupSchema, 
    UserLoginSchema, 
    Status
)

import json
from google.cloud import pubsub_v1

# Se crea una instancia del publisher de Pub/Sub
publisher = pubsub_v1.PublisherClient()

# Se define el ID del proyecto y el nombre del tema así como el nombre de la suscripción
project_id = "uniandes-384423"
subscription_name = "conversion-sub"
topic_name = "conversion"

user_schema = UserSchema()
task_schema = TaskSchema()
signup_schema = UserSignupSchema()


#Se define la variable de ambiente para las credenciales
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'uniandes_cloud_storage.json'
storage_client = storage.Client()
bucket_name = 'conversion-uniandes'

upload_folder = 'upload'
download_folder = 'download'

def upload_to_bucket(blob_name, file_path):
        try:
            bucket = storage_client.get_bucket(bucket_name) 
            blob = bucket.blob(upload_folder+'/'+blob_name)
            blob.upload_from_filename(file_path)
            print(bucket)
            print(blob)
            print(upload_folder)
            print(blob_name)
        except Exception as e:
            #Guardar en el log
            print(e)
            return
        
# Se crea la carpeta para subir los archivos
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)
    print("Creada carpeta {} exitosamente.".format(upload_folder))

# Se crea la carpeta para descargar los archivos convertidos
if not os.path.exists(download_folder):
    os.mkdir(download_folder)
    print("Creada carpeta {} exitosamente.".format(download_folder))

class SignupView(Resource):
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
        
class LoginView(Resource):
    def post(self):
        try:
            # Obtenemos el request body y lo deserializamos con Marshmallow
            login_data = UserLoginSchema().load(request.json, session=db.session)
            user = User.query.filter_by(username=login_data.username).first()
            
            # Si no se emcuentra el usuario o la contraseña es incorrecta se devuelve un error
            if not user:
                return {"message": "User not found"}, 404
            
            if user.password != login_data.password:
                return {"message": "Incorrect password"}, 401
            
            # Si todo es correcto se crea un token jwt
            access_token = create_access_token(identity=user.username, expires_delta=timedelta(hours=2))
            return {"access_token": access_token}, 200
            
        except ValidationError as e:
            return {"message": e.messages}, 400

class UserListView(Resource):
    @jwt_required()
    def get(self):
        return [user_schema.dump(user) for user in User.query.all()]
    
class TaskView(Resource):
    @jwt_required()
    def get(self, id_task):
        return task_schema.dump(Task.query.get_or_404(id_task))
    
    @jwt_required()
    def delete(self, id_task):
        # Obtener la tarea que se quiere eliminar
        task = Task.query.get_or_404(id_task)

        # Borrarla de la base de datos
        db.session.delete(task)
        db.session.commit()
        
        return '',204

class TaskListView(Resource):
    @jwt_required()
    def get(self):
        # Se obtiene el usuario que está logueado
        current_username = get_jwt_identity()
        user = User.query.filter_by(username=current_username).first()

        # Obtener los parámetros de la solicitud en caso de que sean enviados
        max_results = request.args.get('max', default=None, type=int)
        order_by = request.args.get('order', default=None, type=int)

        # Construir una nueva consulta a partir de la relación 'tasks' del usuario
        tasks_query = db.session.query(Task).filter(Task.user == user.id)
        
        # Ordenar las tareas según el parámetro order_by
        if order_by is not None:
            tasks_query = tasks_query.order_by(Task.id.asc() if order_by == 0 else Task.id.desc())
        
        # Filtrar la cantidad de resultados según el parámetro max_results
        if max_results is not None:
            tasks_query = tasks_query.limit(max_results)
        
        # Ejecutar la consulta y devolver las tareas serializadas
        tasks = tasks_query.all()

        return [task_schema.dump(tasks, many=True)]
    
    @jwt_required()
    def post(self):
        # Se obtiene el usuario que está logueado
        current_username = get_jwt_identity()
        user = User.query.filter_by(username=current_username).first()

        # Se cargan los valores de ka ruta del archivo y la nueva extensión 
        file_name = request.files["fileName"]
        new_format = request.form["newFormat"]

        # Copiar el archivo a la carpeta "Upload"
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        # Obtener el nombre base del archivo sin la extensión
        name_base, extension = os.path.splitext(file_name.filename)
        new_file_name = "{}_{}{}".format(name_base, timestamp, extension)
        file_path = os.path.join(upload_folder, new_file_name)
        file_name.save(file_path)

        #Guardar en el bucket
        upload_to_bucket(new_file_name, file_path)
    
        # Se crea la nueva tarea en base de datos
        new_task = Task(fileName=new_file_name, newFormat=new_format)
        new_task.user = user.id
        db.session.add(new_task)
        db.session.commit()

        # Crea un diccionario JSON para enviar la información de la tarea a procesar
        data = {
            'taskId': new_task.id,
            'taskFilename': new_task.fileName,
            'taskNewFormat': new_task.newFormat
        }

        topic_path = publisher.topic_path(project_id, topic_name)

        # Se convierte el diccionario JSON en una cadena de texto
        json_data = json.dumps(data)

        # Se publica el mensaje en el tema
        publisher.publish(topic_path, data=json_data.encode('utf-8'))

        return {"message": "Tarea encolada satisfactoriamente."}, 201
    
    
    
class FileView(Resource):
    @jwt_required()
    def get(self, filename):
        # Se utiliza os.path.join para establecer la ruta
        input_file_path = os.path.join(os.getcwd(), upload_folder, filename)

        # Se utiliza os.path.join para establecer la ruta
        output_file_path = os.path.join(os.getcwd(), download_folder, filename)

        # Revisar si existe el archivo
        if os.path.exists(input_file_path):
            # Se utiliza send_file para retornar el archivo
            return send_file(input_file_path, as_attachment=True)
        elif os.path.exists(output_file_path):
            # Se utiliza send_file para retornar el archivo
            return send_file(output_file_path, as_attachment=True)
        else:
            return {"Error": "Archivo no encontrado. Ruta: {}".format(os.getcwd())}, 404
          
            
class ProcessView(Resource):
    def get(self):
        # Tareas con estado 'UPLOADED'
        uploaded_tasks_query = db.session.query(Task).filter(Task.status == Status.UPLOADED)
        
        # Devolver las tareas serializadas
        tasks = uploaded_tasks_query.all()

        processed_tasks = 0

        for task in tasks:
            compress_file(task.fileName, task.newFormat)
            task.status = Status.PROCESSED
            db.session.commit()
            processed_tasks += 1

        return {"Message": "Procesadas {} tareas".format(processed_tasks)}, 200
       
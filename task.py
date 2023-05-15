from datetime import timedelta
from celery import Celery
import time, json

# sqlalchemy libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

# functions
from tasks import compress_file

# pub-sub
from google.cloud import pubsub_v1

# Crea una instancia del cliente
subscriber = pubsub_v1.SubscriberClient()

# Crea una instancia del cliente
publisher = pubsub_v1.PublisherClient()

# configuracion postgresq
engine = create_engine('postgresql://postgres:SN4kRspz%7#cb^;u@10.32.80.3/cloud_conversion')

session = Session(bind=engine)

Base = declarative_base()

from models import (
    Task,
    Status
)

app = Celery( 'task' , broker = 'redis://localhost:6379/0' ) 

app.conf.beat_schedule = {
    'mi-tarea-diaria': {
        'task': 'task.traer_tareas',
        #'args': (2, 5),
        'schedule': timedelta(seconds=30)
    },
}

def process_message(message):
    # Decodifica el mensaje recibido
    json_data = message.data.decode('utf-8')

    # Convierte el JSON en un objeto Python
    data = json.loads(json_data)

    # Realiza las operaciones necesarias con los datos recibidos
    print('Mensaje recibido:', data)

    gestionar_tarea(data.taskId)

    # Marca el mensaje como procesado
    message.ack()

def subscribe(project_id, subscription_name):
    # Forma el nombre completo de la suscripción
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        process_message(message)

    # Inicia la suscripción y establece la función de callback
    subscriber.subscribe(subscription_path, callback=callback)

    # Espera a que lleguen mensajes
    print(f"Escuchando mensajes en la suscripción: {subscription_name}")
    while True:
        time.sleep(1)

project_id = "uniandes-384423"
subscription_name = "conversion-sub"
topic_name = "conversion"

# def publish_message(project_id, topic_name):
#     # Forma el nombre completo del tema
#     topic_path = publisher.topic_path(project_id, topic_name)

#     # Define el mensaje de prueba
#     message = "Cloud Team 23"

#     # Publica el mensaje de prueba
#     future = publisher.publish(topic_path, data=message.encode("utf-8"))
#     print(f"Mensaje de prueba publicado: {message}")
#     return future.result()

#publish_message(project_id, topic_name)

# Creamos una tarea llamada sumar_numeros usando el decorador @app.task
# Se imprime un mensaje con la fecha simulando un LOG
@app.task
def traer_tareas():
    #  # Tareas con estado 'UPLOADED'
    uploaded_tasks_query = session.query(Task).filter(Task.status == Status.UPLOADED)

    # Devolver las tareas serializadas
    tasks = uploaded_tasks_query.all()

    processed_tasks = 0

    print("hola mundo desde colombia para todo el mundo")

    for task in tasks:
        compress_file(task.fileName, task.newFormat)
        task.status = Status.PROCESSED
        session.commit()
        processed_tasks += 1

def gestionar_tarea(taskId):
    #  # Tareas con estado 'UPLOADED'
    task_query = session.query(Task).filter(Task.id == taskId)

    # Devolver las tareas serializadas
    task = task_query.first()

    compress_file(task.fileName, task.newFormat)
    task.status = Status.PROCESSED
    session.commit()

subscribe(project_id, subscription_name)
from datetime import datetime, timedelta
from celery import Celery
from celery.schedules import crontab

# sqlalchemy libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

# functions
from tasks import compress_file


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
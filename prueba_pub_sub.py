import json
from google.cloud import pubsub_v1
from google.oauth2 import service_account
import os
import time

project_id = "uniandes-384423"
subscription_name = "conversion-sub"
topic_name = "conversion"


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
# try:
#     info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
#     print(info)
#     GS_CREDENTIALS = service_account.Credentials.from_service_account_info(info)
# except Exception as e:
#     print(e)
#     print("hay un error")
#     GS_CREDENTIALS = None

# # Se crea una instancia del publisher de Pub/Sub
# publisher = pubsub_v1.PublisherClient(credentials=GS_CREDENTIALS)


# topic_path = publisher.topic_path(project_id, topic_name)

# data = {
#     "mnsj": "Hola mundo",
#     "prueba": "desde el servidor"
# }

# # Se convierte el diccionario JSON en una cadena de texto
# json_data = json.dumps(data)

# # Se publica el mensaje en el tema
# publisher.publish(topic_path, data=json_data.encode('utf-8'))



# def process_message(message):
#     # # Decodifica el mensaje recibido
#     json_data = message.data.decode('utf-8')

#     # # Convierte el JSON en un objeto Python
#     data = json.loads(json_data)

#     # Realiza las operaciones necesarias con los datos recibidos
#     print('Mensaje recibido:', message.data)

#     # gestionar_tarea(data.taskId)

#     # Marca el mensaje como procesado
#     message.ack()

# def subscribe(project_id, subscription_name):
#     subscriber = pubsub_v1.SubscriberClient()
#     # Forma el nombre completo de la suscripción
#     subscription_path = subscriber.subscription_path(project_id, subscription_name)

#     def callback(message):
#         process_message(message)

#     # Inicia la suscripción y establece la función de callback
#     subscriber.subscribe(subscription_path, callback=callback)

#     # Espera a que lleguen mensajes
#     print(f"Escuchando mensajes en la suscripción: {subscription_name}")
#     while True:
#         time.sleep(1)

# subscribe(project_id,subscription_name)
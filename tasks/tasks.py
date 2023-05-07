# from celery import Celery
import zipfile
import py7zr
import tarfile
import os

# celery = Celery('convert', broker='redis://localhost:6379/0')

# Imports the Google Cloud client library
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'uniandes_cloud_storage.json'

#Se define la variable de ambiente para las credenciales
storage_client = storage.Client()
bucket_name = 'conversion-uniandes'

# Directorio de origen y destino para los archivos
input_dir = "upload/"
output_dir = 'download/'

def upload_to_bucket(blob_name, file_path):

    bucket = storage_client.get_bucket(bucket_name) 

    # como va a quedar en google
    blob = bucket.blob(file_path)
    # como se llama localmente
    blob.upload_from_filename(file_path)

def download_file_from_bucket(file_name, file_path):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob('upload/'+file_name)
    blob.download_to_filename('upload/'+file_name)

# @celery.task()
def compress_file(filename, output_format):
    
    # Verificar que el formato de salida es válido
    output_format = output_format.lower()
    if output_format not in ["zip", "7z", "tar.bz2"]:
        raise ValueError("Formato de salida no válido")

    # Obtener la ruta del archivo de entrada
    input_path = os.path.join(input_dir, filename)

    download_file_from_bucket(filename, input_dir)

    # # Verificar que el archivo de entrada existe
    # if not os.path.isfile(input_path):
    #     raise FileNotFoundError(f"El archivo {filename} no existe en {input_dir}")

    # Comprimir el archivo de entrada y guardarlo en la carpeta de salida
    output_filename = os.path.splitext(filename)[0] + "." + output_format
    output_path = os.path.join(output_dir, output_filename)
    if output_format == "zip":
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(input_path, arcname=filename)
            upload_to_bucket(filename, output_path)
    elif output_format == "7z":
        with py7zr.SevenZipFile(output_path, "w") as z:
            z.write(input_path, arcname=filename)
            upload_to_bucket(filename, output_path)
    elif output_format == "tar.bz2":
        with tarfile.open(output_path, "w:bz2") as t:
            t.add(input_path, arcname=filename)
            upload_to_bucket(filename, output_path)
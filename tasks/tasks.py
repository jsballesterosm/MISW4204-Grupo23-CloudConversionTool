# from celery import Celery
import zipfile
import py7zr
import tarfile
import os

# celery = Celery('convert', broker='redis://localhost:6379/0')

# Directorio de origen y destino para los archivos
input_dir = "upload/"
output_dir = 'download/'

# @celery.task()
def compress_file(filename, output_format):
    
    # Verificar que el formato de salida es válido
    output_format = output_format.lower()
    if output_format not in ["zip", "7z", "tar.bz2"]:
        raise ValueError("Formato de salida no válido")

    # Obtener la ruta del archivo de entrada
    input_path = os.path.join(input_dir, filename)

    # Verificar que el archivo de entrada existe
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"El archivo {filename} no existe en {input_dir}")

    # Comprimir el archivo de entrada y guardarlo en la carpeta de salida
    output_filename = os.path.splitext(filename)[0] + "." + output_format
    output_path = os.path.join(output_dir, output_filename)
    if output_format == "zip":
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(input_path, arcname=filename)
    elif output_format == "7z":
        with py7zr.SevenZipFile(output_path, "w") as z:
            z.write(input_path, arcname=filename)
    elif output_format == "tar.bz2":
        with tarfile.open(output_path, "w:bz2") as t:
            t.add(input_path, arcname=filename)
# MISW4204-Grupo15-CloudConversionTool
Se realiza la configuración en la aplicación para trabajar con Docker-Compose el despliegue de la aplicación:

📦 MISW4204-Grupo23-CloudConversionTool<br>
┣---- 📂 models<br>
┃     ┗---- 📜 __init__.py<br>
┃     ┗---- 📜 model.py<br>
┣---- 📂 tasks<br>
┃     ┗---- 📜 __init__.py<br>
┃     ┗---- 📜 tasks.py<br>
┣---- 📂 view<br>
┃     ┗---- 📜 __init__.py<br>
┃     ┗---- 📜 view.py<br>
┗---- 📜 .dockerignore<br>
┗---- 📜 .gitignore<br>
┗---- 📜 converter.py<br>
┗---- 📜 docker-compose.yml<br>
┗---- 📜 Dockerfile<br>
┗---- 📜 Readme.md<br>
┗---- 📜 requeriments.txt<br>
┗---- 📜 wsgy.py
 
Por último, se realiza la configuración para ejecutar el Docker-compose en el archivo Docker-compose.yml
 
![Archivoyml](https://user-images.githubusercontent.com/98661682/232351674-3d31cd7a-7ff6-464e-9a33-8aefc2b271df.png)

Ejecución del Docker-compose
- Debemos tener instalado en el servidor docker y docker-compose
En la ruta raíz del proyecto ejecutamos la sentencia para subir el docker-compose
     - sudo docker-compose up 
    si queremos recompilar el proyecto se debe añadir la sentencia "--build" al final del comando anterior
    Para bajar y remover los contenedores ejecutamos la sentencia
     - sudo docker-compose down 

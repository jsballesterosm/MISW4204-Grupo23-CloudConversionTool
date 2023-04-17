# MISW4204-Grupo15-CloudConversionTool
Se realiza la configuración en la aplicación para trabajar con Docker-Compose el despliegue de la aplicación:

📦 MISW4204-Grupo23-CloudConversionTool
 ┣---- 📂 models
 ┃     ┗---- 📜 __init__.py
 ┃     ┗---- 📜 model.py
 ┣---- 📂 tasks
 ┃     ┗---- 📜 __init__.py
 ┃     ┗---- 📜 tasks.py
 ┣---- 📂 view
 ┃     ┗---- 📜 __init__.py
 ┃     ┗---- 📜 view.py
 ┗---- 📜 .dockerignore [x]
 ┗---- 📜 .gitignore
 ┗---- 📜 converter.py
 ┗---- 📜 docker-compose.yml [x]
 ┗---- 📜 Dockerfile
 ┗---- 📜 Readme.md [x]
 ┗---- 📜 requeriments.txt
 ┗---- 📜 wsgy.py [x]
 
Por último, se realiza la configuración para ejecutar el Docker-compose en el archivo Docker-compose.yml
 


Ejecución del Docker-compose
•	Debemos tener instalado en el servidor docker y docker-compose 
    En la ruta raíz del proyecto ejecutamos la sentencia para subir el docker-compose
    •	sudo docker-compose up 
    si queremos recompilar el proyecto se debe añadir la sentencia "--build" al final del comando anterior
    Para bajar y remover los contenedores ejecutamos la sentencia
    •	sudo docker-compose down 

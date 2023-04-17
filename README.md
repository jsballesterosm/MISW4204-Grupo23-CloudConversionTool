# MISW4204-Grupo15-CloudConversionTool

## Estructura del proyecto
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
 
## Instalación Herramientas
### Docker
```shell
sudo apt install docker-ce
```
### Docker-Compose
```shell
 - sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Se realiza la configuración en el ambiente de desarrollo para ejecutar el Docker-compose mediante el archivo Docker-compose.yml
 
![Archivoyml](https://user-images.githubusercontent.com/98661682/232351674-3d31cd7a-7ff6-464e-9a33-8aefc2b271df.png)

Realizada la instalación y configuración de la aplicación para trabajar con Docker-Compose se realiza el despliegue de la aplicación:

## Ejecución del Docker-compose
- Debemos tener instalado en el servidor docker y docker-compose
En la ruta raíz del proyecto ejecutamos la sentencia para subir el docker-compose
    ```shell
    sudo docker-compose up 
    ```
    si queremos recompilar el proyecto se debe añadir la sentencia "--build" al final del comando anterior
    ```shell
    sudo docker-compose up --build
    ```
    Verificamos que los contenedores se encuentren en ejecución
    ```shell
    sudo docker ps
    ```    
    Para bajar y remover los contenedores ejecutamos la sentencia
    ```shell
    sudo docker-compose down  
    ```

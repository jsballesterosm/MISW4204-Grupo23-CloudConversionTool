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
    Resultado del comando
![image](https://user-images.githubusercontent.com/98661682/232354266-512b0316-f0ca-4152-9492-f76367be8837.png)
    
    Para bajar y remover los contenedores ejecutamos la sentencia
    ```shell
    sudo docker-compose down  
    ```

## Ejecución del cronjob - proceso asincrónico
Se realiza la creación de un cronjob que ejecuta el endpoint para procesar los archivos "http//:URL/api/process"

![image](https://user-images.githubusercontent.com/98661682/232353520-ea4c530c-8177-47a4-b819-46d611e6ba05.png)



# celery

- redis server
- celery -A task worker -B --loglevel=info

# configurar celery y redis
sudo apt-get install redis-server


# Paso a paso configuración balanceador de carga
gcloud compute instance-groups managed create lb-backend-conversion-tool-group --template=lbl-template-backend-conversion --size=3 --zone=us-west1-a


## Template disco
lbl-template-blackend-conversion-tool

## imagen
lbl-template-backend-conversion

### aqui creamos la regla

```shell
 gcloud compute firewall-rules create fw-allow-health-check \
   --network=network-uniandes \
   --action=allow \
   --direction=ingress \
   --source-ranges=34.105.0.0/22,34.168.0.0/16,104.198.0.0/16 \
   --target-tags=allow-health-check \
   --rules=tcp:80
```



### creamos ip principal para el balanceo
  ```shell
  gcloud compute addresses create lb-ipv4-1 \
    --ip-version=IPV4 \
    --global
  ```

## ip resultante
```shell
34.160.199.235 
```
## creacion de verificion de estado
```shell
gcloud compute health-checks create http http-basic-check --port 80
```

## creacion de servicio backend
```shell
gcloud compute backend-services create web-backend-service \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=http-basic-check \
  --global
```  

## asociamos el grupo de instancias previamente creado
## al servicio backend
```shell
gcloud compute backend-services add-backend web-backend-service \
  --instance-group=lb-backend-conversion-tool-group \
  --instance-group-zone=us-west1-a \
  --global
```    


## creamos el mapa de urls para enturar el servicio 
## de backend
```shell
gcloud compute url-maps create web-map-http \
    --default-service web-backend-service
```    

## creamos el proxy http para enrutar 
```shell
gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map-http
```     

## Crea una regla de reenvío global para enrutar las solicitudes entrantes al proxy
```shell
gcloud compute forwarding-rules create http-content-rule \
    --address=lb-ipv4-1\
    --global \
    --target-http-proxy=http-lb-proxy \
    --ports=80
``` 

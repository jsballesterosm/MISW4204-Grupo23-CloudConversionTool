## PASO A PASO EJECUCION DE PRUEBAS CON APACHE BENCH

### Permisos al archivo init
```shell
chmod +ux init.sh
```
### Ejecutar pruebas de cargas y de concurrencia
```shell
./init.sh <TOKEN> <URL_TASK> 
```

Pasamos como parametro el token bearer y el url donde se va a realizar la comprobacion

Ejemplo:
```shell
./init.sh eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTkxNzMwOSwianRpIjoiMjkwNGVhOGUtOGRmZC00ZTdlLWFkMGEtNzkzYWYxNGZjN2RkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNpc3RlbWFzIiwibmJmIjoxNjgxOTE3MzA5LCJleHAiOjE2ODE5MjQ1MDl9.e2XsdQ1P_A5Qp1TyNZl16keAGBmgCnuEpDcmnqImax4 127.0.0.1:5000/api/tasks
```
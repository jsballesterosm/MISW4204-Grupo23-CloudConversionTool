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
./init.sh eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTk1NzI5NSwianRpIjoiNDBjMjFiZjUtZDNkZC00Y2Y0LWJmMzktZDg0OTBhZWY0Yjg4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNpc3RlbWFzIiwibmJmIjoxNjgxOTU3Mjk1LCJleHAiOjE2ODE5NjQ0OTV9.4mFwBuV1I0e3IsxAnpuf1cJmKZr_4sHou7X_9kz40Cs 127.0.0.1:5000/api/tasks
```
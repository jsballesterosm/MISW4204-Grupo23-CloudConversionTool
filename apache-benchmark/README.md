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
./init.sh eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTk0ODAxMSwianRpIjoiYWQ5ZmE1MzItYzNkMy00YjQ4LThjMDQtN2FlN2ZiNTM1ZjYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNpc3RlbWFzIiwibmJmIjoxNjgxOTQ4MDExLCJleHAiOjE2ODE5NTUyMTF9.SwTrkFTfgjVAokBA9UYycz4gN8yn2iQEQqlFs40oAGw 127.0.0.1:5000/api/tasks
```
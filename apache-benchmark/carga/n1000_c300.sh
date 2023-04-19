echo "\nPRUEBA: n1000 c300"
ab -n 1000 -c 300 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/reportes/n1000_c300.csv  -p request-body.txt $2

gnuplot carga/reportes/n1000_c300.p
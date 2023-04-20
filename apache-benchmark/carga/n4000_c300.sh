echo "\nPRUEBA: n4000 c300"
ab -n 4000 -c 300 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n4000_c300.csv  -p request-body.txt $2

gnuplot carga/conf/n4000_c300.p
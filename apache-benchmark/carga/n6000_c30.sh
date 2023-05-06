echo "\nPRUEBA: n6000 c30"
ab -n 6000 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n6000_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n6000_c30.p
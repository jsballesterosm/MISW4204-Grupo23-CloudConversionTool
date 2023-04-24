echo "\nPRUEBA: n3500 c30"
ab -n 3500 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n3500_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n3500_c30.p
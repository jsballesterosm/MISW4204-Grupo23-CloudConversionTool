echo "\nPRUEBA: n10000 c30"
ab -n 10000 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n10000_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n110000_c30.p
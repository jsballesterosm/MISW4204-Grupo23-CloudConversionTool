echo "\nPRUEBA: n9000 c30"
ab -n 9000 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n9000_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n9000_c30.p
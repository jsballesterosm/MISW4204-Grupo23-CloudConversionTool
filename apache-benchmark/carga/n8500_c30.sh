echo "\nPRUEBA: n8500 c30"
ab -n 8500 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n8500_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n8500_c30.p
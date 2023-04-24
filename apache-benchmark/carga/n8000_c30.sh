echo "\nPRUEBA: n8000 c30"
ab -n 8000 -c 30 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g carga/planos/n8000_c30.csv  -p request-body.txt $2

gnuplot carga/conf/n8000_c30.p
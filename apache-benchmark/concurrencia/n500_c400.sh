echo "\nPRUEBA: n500 c400"
ab -n 500 -c 400 -H "Authorization: Bearer ${1}" -T "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -g concurrencia/planos/n500_c400.csv  -p request-body.txt $2

gnuplot concurrencia/conf/n500_c400.p
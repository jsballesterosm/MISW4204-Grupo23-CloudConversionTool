set terminal png size 600
set output "concurrencia/reportes/reporte_n500_c100.png"
set title "500 peticiones, 100 peticiones concurrentes"
set size ratio 0.6
set grid y
set xlabel "Nro Peticiones"
set ylabel "Tiempo de respuesta (ms)"
plot "concurrencia/planos/n500_c100.csv" using 9 smooth sbezier with lines title "http://ip_servidor/cipher"
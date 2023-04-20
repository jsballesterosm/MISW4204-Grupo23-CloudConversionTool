#!/bin/bash

TOKEN=$1
URL_TASK=$2



echo -e "---"
echo -e "PRUEBAS DE CARGA"
echo "---"

sh carga/n1000_c300.sh ${1} ${2}

sh carga/n2000_c300.sh ${1} ${2}

sh carga/n3000_c300.sh ${1} ${2}

sh carga/n4000_c300.sh ${1} ${2}

sh carga/n5000_c300.sh ${1} ${2}

echo -e "---"
echo -e "PRUEBAS DE CONCURRENCIA"
echo "---"

sh concurrencia/n500_c100.sh ${1} ${2}

sh concurrencia/n500_c200.sh ${1} ${2}

sh concurrencia/n500_c300.sh ${1} ${2}

sh concurrencia/n500_c400.sh ${1} ${2}

sh concurrencia/n500_c500.sh ${1} ${2}
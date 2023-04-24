#!/bin/bash

TOKEN=$1
URL_TASK=$2

TIME_SLEEP=1

echo -e "---"
echo -e "PRUEBAS DE CARGA"
echo "---"

sh carga/n500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n1000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n1500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n2000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n2500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n3000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n3500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n4000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n4500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n5000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n5500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n6000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n6500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n7000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n7500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n8000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n8500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n9000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n9500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n10000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n10500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n11000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n11500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n12000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n12500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n13000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n13500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n14000_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n14500_c30.sh ${1} ${2}

sleep $TIME_SLEEP

sh carga/n15000_c30.sh ${1} ${2}
#!/bin/bash

TOKEN=$1
URL_TASK=$2



echo -e "---"
echo -e "PRUEBAS DE CARGA"
echo "---"

sh carga/n5000_c300.sh ${1} ${2}

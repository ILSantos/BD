#!/bin/bash

echo "Instalando Python 3.7..."

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7 python3.7-dev curl -y

echo "Instalando pip sobre o Python 3.7..."

curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python3.7 get-pip.py

python3.7 -m pip install --upgrade pip setuptools wheel

echo "Instalando dependencias..."

pip install PyInquirer psycopg2 terminalplot

echo "Pronto, ambiente configurado."
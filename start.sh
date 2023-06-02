#!/bin/bash
echo "Démarrage en cours ..."
echo "Installations des dépendances ..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 run_app.py
echo "Fin du programme"
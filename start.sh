#!/bin/bash
echo "Démarrage en cours ..."
echo "Installations des dépendances ..."
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python3 run_app.py
echo "Fin du programme"
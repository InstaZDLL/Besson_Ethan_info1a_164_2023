#!/bin/bash
echo "Démarrage en cours ..."
echo "Installations des dépendances ..."
pip install -r requirements.txt
python3 run_app.py
echo "Fin du programme"
@echo off
echo "Démarrage en cours ..."
echo "Installations des dépendances ..."
pip install -r requirements.txt
python.exe run_app.py
echo "Fin du programme"
pause
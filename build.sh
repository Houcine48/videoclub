#!/usr/bin/env bash
# Exit on error
set -o errexit

# Installer les outils
pip install -r requirements.txt

# Rassembler les fichiers CSS/Images
python manage.py collectstatic --no-input

# Mettre a jour la base de donnees
python manage.py migrate
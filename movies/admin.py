from django.contrib import admin
from .models import Movie

# On dit à l'admin : "Gère ce modèle s'il te plaît"
admin.site.register(Movie)
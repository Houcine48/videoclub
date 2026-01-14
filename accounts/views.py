from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        # Si on a envoyé le formulaire rempli
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # On crée l'utilisateur
            return redirect('home') # On retourne à l'accueil
    else:
        # Si on arrive juste sur la page (formulaire vide)
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
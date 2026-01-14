from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from .models import Rental

@login_required
def rent_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Rental.objects.create(user=request.user, movie=movie)
    return redirect('my_rentals') # <--- J'ai change ca : on va vers "mes locations"

@login_required
def my_rentals(request):
    # On cherche les locations de l'utilisateur connecte
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'my_rentals.html', {'rentals': rentals})
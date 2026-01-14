from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Wishlist # <--- J'ai ajoute Wishlist

def movie_list(request):
    query = request.GET.get('search')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    
    # Gestion de l'ajout d'avis
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(movie=movie, user=request.user, rating=rating, comment=comment)
        return redirect('detail', id=movie.id)

    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})

# --- NOUVEAU : Ajouter a la wishlist ---
@login_required
def add_to_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # On cree l'entree (si elle n'existe pas deja)
    Wishlist.objects.get_or_create(user=request.user, movie=movie)
    return redirect('my_wishlist')

# --- NOUVEAU : Voir ma wishlist ---
@login_required
def my_wishlist(request):
    # On recupere les souhaits de l'utilisateur
    wishes = Wishlist.objects.filter(user=request.user)
    return render(request, 'my_wishlist.html', {'wishes': wishes})
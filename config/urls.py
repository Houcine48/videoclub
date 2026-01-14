from django.contrib import admin
from django.urls import path
from movies.views import movie_list, movie_detail, add_to_wishlist, my_wishlist # <--- Ajouts
from accounts.views import register
from django.contrib.auth import views as auth_views
from rentals.views import rent_movie, my_rentals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_list, name='home'),
    path('movie/<int:id>/', movie_detail, name='detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('rent/<int:movie_id>/', rent_movie, name='rent_movie'),
    path('my-rentals/', my_rentals, name='my_rentals'),
    
    # --- NOUVEAU ---
    path('wishlist/add/<int:movie_id>/', add_to_wishlist, name='add_wishlist'),
    path('my-wishlist/', my_wishlist, name='my_wishlist'),
]
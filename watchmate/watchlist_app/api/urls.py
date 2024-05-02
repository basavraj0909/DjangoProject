from django.urls import path, include

# from watchmate import watchlist_app
"""CLASS BASED VIEW"""
from .views import MovielistView, MovieDetailView
urlpatterns = [
    path('list/', MovielistView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
]

"""FUNCTION BASED VIEW"""
# from .views import movie_list, movie_detail
# urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),
# ]

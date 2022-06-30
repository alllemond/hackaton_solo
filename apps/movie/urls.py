
from django.urls import path
from .views import MovieListView, CreateMovieView, RetrieveEditDestroyMovieView 

urlpatterns = [
    path('', MovieListView.as_view()),
    path('film/', CreateMovieView.as_view()),
    path('film/<int:pk>/', RetrieveEditDestroyMovieView.as_view()),
]
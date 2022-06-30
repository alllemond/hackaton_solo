
from rest_framework.viewsets import ModelViewSet
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieSerializer
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
from rest_framework import filters,generics 

# from .filters import PublicationDateFilter



# APiView
# genericview
# ModelViewSet



class CreateMovieView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    serializer_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveEditDestroyMovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
    search_fields = ['title']

    def get_serializer_context(self):
        return {'request': self.request}
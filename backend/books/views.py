from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from books.serializers import BookSerializer

from books.models import Book


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "series", "author",
                        "artist", "publisher", "translator"]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.

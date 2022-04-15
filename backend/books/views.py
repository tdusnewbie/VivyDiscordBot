from django.shortcuts import render
from rest_framework import generics

from books.serializers import BookSerializer

from books.models import Book


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.

from rest_framework import serializers

from books.models import Book


class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "series", "date_published", "publisher",
                  "author", "artist", "translator", "price"]

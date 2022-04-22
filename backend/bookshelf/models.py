from django.db import models
from books.models import Book


class BookShelf(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(
        "auth.User", related_name="bookshelfs", on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name="bookshelfs")

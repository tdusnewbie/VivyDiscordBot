from pyexpat import model
from django.db import models


class Book(models.Model):
    name = models.TextField()
    # series =
    author = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100, null=True)
    date_published = models.DateField()
    # publisher =
    translator = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0)

    class Meta:
        ordering = ["name", "date_published"]

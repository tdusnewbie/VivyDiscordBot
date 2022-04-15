from django.urls import path, include
from books import views

urlpatterns = [
    path("", views.BookList.as_view(), name="book-list-create"),
    path("<int:pk>/", views.BookDetail.as_view(),
         name="book-retrieve-update-destroy"),
]

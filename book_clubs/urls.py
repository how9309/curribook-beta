from django.urls import path

from . import views

app_name = "book_clubs"

urlpatterns = [
    path("", views.BookReviewView.as_view(), name="review"),
    path("<int:pk>", views.BookReviewDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditBookReviewView.as_view(), name="edit"),
    path("list/", views.BookClubListView.as_view(), name="home"),
    path("list/england", views.EnglandView.as_view(), name="england"),
    path("list/dog", views.DogView.as_view(), name="dog"),
    path("list/consumer", views.ConsumerView.as_view(), name="consumer"),
    path("list/think", views.ThinkView.as_view(), name="think"),
    path("create/", views.CreateBookReviewView.as_view(), name="create"),
]

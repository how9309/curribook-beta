from django.urls import path

from . import views

app_name = "curriculums"

urlpatterns = [
    path("<int:pk>", views.CurriculumDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("category/lifestyle", views.LifestyleView.as_view(), name="lifestyle"),
    path("category/travel", views.TravelView.as_view(), name="travel"),
    path("category/knowledge", views.KnowledgeView.as_view(), name="knowledge"),
    path("category/fiction", views.FictionView.as_view(), name="fiction"),
    path("nav/", views.NavView.as_view(), name="nav"),
    path("application/", views.post, name="application"),

]

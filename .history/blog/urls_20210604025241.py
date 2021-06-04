from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all, name="home"),
    path("article/<str:id>", views.get_article),
    path("search_article/", views.search_article),
    path("search_article/<str:title>", views.search_article)
]

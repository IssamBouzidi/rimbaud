from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.get_all),
    path("article/<str:id>", views.get_article),
    path("search_article/", views.search_article),
    re_path("search_article/<str:text>", views.search_article)
]

from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.get_all),
    path("article/<str:id>", views.get_article),
    #path("search_article/<str:text>", views.search_article),
    path(r'^search_article/(?P<text>/$)', views.search_article)
]

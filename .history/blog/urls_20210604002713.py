from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all),
    path("article/<str:id>", views.get_article),
    #path("search_article/<str:text>", views.search_article),
    path(r'^search_article/(?P<str:text>\w+)', views.search_article)
]

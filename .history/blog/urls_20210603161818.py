from django.urls import path

from . import views

urlpatterns = [
    #path("", views.home),
    path("", views.get_all),
    path("article/<str:id>", views.get_article),
]

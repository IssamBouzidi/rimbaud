from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("all", views.get_all),
    path("<int:id>", views.article)
]

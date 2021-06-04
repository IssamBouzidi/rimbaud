from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.get_all, name="home"),
    path("article/<str:id>", views.get_article),
    path("search_article/<str:title>", views.search_article)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

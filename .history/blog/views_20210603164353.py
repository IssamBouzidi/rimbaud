from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.db.models.query import QuerySet
import datetime


def home(request) -> HttpResponse:
    return HttpResponse("Hello, welcome to my blog!")



def get_all(request) -> HttpResponse:
    articles = __default_articles_query(request.user.is_superuser)

    context = {"articles_view_title": "Welcome on my page", "articles": articles}
    return render(request, "all.html", context)


def get_article(request, id: str) -> HttpResponse:
    if id.isnumeric():
        article = (
            __default_articles_query(request.user.is_superuser).filter(id=id).first()
        )
    else:
        article = None

    if article is None:
        return render(request, "not_exists.html")

    context = {"article": article}
    return render(request, "article.html", context)


def search_article(request, text: str = None) -> HttpResponse:
    if text is None:
        articles = __default_articles_query(request.user.is_superuser)
    else:
        articles = __default_articles_query(request.user.is_superuser).filter(
            title__icontains=text
        )

    list_articles = {"articles": articles}
    return render(request, "detail_article.html", list_articles)


def __default_articles_query(is_admin: bool = False) -> QuerySet:
    articles = Article.objects.exclude(
        visibility_date_limit__lt=datetime.datetime.now(),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            visible_only_by_admin=True,
        )

    return articles


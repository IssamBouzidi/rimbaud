from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.db.models.query import QuerySet
import datetime


def get_all(request) -> HttpResponse:
    articles = __find_articles_query(request.user.is_superuser)
    list_articles = {"articles": articles}
    return render(request, "all.html", list_articles)


def get_article(request, id: str) -> HttpResponse:
    print(f'id: {id.__class__.__name__}')
    if id.isnumeric():
        article = (
            __find_articles_query(request.user.is_superuser).filter(id=id).first()
        )
    else:
        article = None

    if article is None:
        return render(request, "not_exists.html")

    context = {"article": article}
    return render(request, "article.html", context)


def search_article(request, title: str = None) -> HttpResponse:
    if title is None:
        articles = __find_articles_query(request.user.is_superuser)
    else:
        articles = __find_articles_query(request.user.is_superuser).filter(
            title__icontains=title
        )

    context = {"articles": articles}
    return render(request, "detail_article.html", context)


def __find_articles_query(is_admin: bool = False) -> QuerySet:
    articles = Article.objects.exclude(
        visibility_date_limit__lt=datetime.datetime.now(),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            visible_only_by_admin=True,
        )

    return articles


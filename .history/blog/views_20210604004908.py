from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.db.models.query import QuerySet
import datetime


def get_all(request) -> HttpResponse:
    query = __find_articles_query(request.user.is_superuser)
    articles_list = {"articles": query}
    return render(request, "all.html", articles_list)


def get_article(request, id: str) -> HttpResponse:
    print(f'id: {id.__class__.__name__}')
    query = (__find_articles_query(request.user.is_superuser).filter(id=id).first())
    article = {"article": query}
    return render(request, "article.html", article)


def search_article(request, title: str = None) -> HttpResponse:
    if title is None:
        query = __find_articles_query(request.user.is_superuser)
    else:
        query = __find_articles_query(request.user.is_superuser).filter(
            title__icontains=title
        )

    articles_list = {"articles": query}
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


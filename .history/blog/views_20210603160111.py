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
    return render(request, "view_all.html", context)



def __default_articles_query(is_admin: bool = False) -> QuerySet:
    articles = Article.objects.exclude(
        # filter articles with validity date > today (arrange server date to utc)
        visibility_date_limit>datetime.datetime.now(),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            visible_only_by_admin=True,
        )

    return articles


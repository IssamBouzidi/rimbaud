from django.shortcuts import render
from django.http import HttpResponse
from blog import Article
from django.db.models.query import QuerySet
import datetime


def all(request) -> HttpResponse:
    """Main page. Display all articles

    Args:
        request ([HttpRequest]): -

    Returns:
        [HttpResponse]: list of articles
    """
    articles = __default_articles_query(request.user.is_superuser)

    context = {"articles_view_title": "Welcome on my page", "articles": articles}
    return render(request, "view_all.html", context)



def __default_articles_query(is_admin: bool = False) -> QuerySet:
    """[summary]

    Args:
        is_admin (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    articles = Article.objects.exclude(
        # filter articles with validity date > today (arrange server date to utc)
        end_date__lt=datetime.datetime.now(),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            is_adm_only=True,
        )

    return articles


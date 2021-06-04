from django.shortcuts import render
from django.http import HttpResponse
from blog import Article

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


from django.db import models


class Article(models.Model):
    title = models.CharField("Titre")
    description = models.CharField("Déscription")
    article = models.CharField("Article", max_length=5000)
    visibility_date_limit = models.DateTimeField("Date limite de parution")
    visible_only_by_admin = models.BooleanField("Article visible par l'administrateur uniquement", default=True)
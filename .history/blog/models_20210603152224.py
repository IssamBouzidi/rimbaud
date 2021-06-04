from django.db import models


class Article(models.Model):
    title = models.CharField("Titre", max_length=25)
    description = models.CharField("Déscription", max_length=50)
    article = models.TextField("Article", max_length=250)
    visibility_date_limit = models.DateField("Date limite de parution")
    visible_only_by_admin = models.BooleanField("Article visible par l'administrateur uniquement", default=True)
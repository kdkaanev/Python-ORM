from django.db import models
from django.db.models import Sum


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):

        return self.annotate(total_article=Sum('article')).order_by('-total_article', 'email').all()

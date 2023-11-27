import os
import django
from django.db.models import Q, Sum, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Author, Article


# Import your models here
# Create and run your queries within functions
def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    autors = Author.objects.filter(
        Q(full_name__icontains=search_name)
            or
        Q(email__icontains = search_email)
    ).order_by('-full_name')
    result = []

    for author in autors:
        status = 'Banned' if author.is_banned else 'Not Banned'
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return '\n'.join(result)


def get_top_publisher():
    publisher = Author.objects.get_authors_by_article_count().order_by('email').first()
    if publisher is None:
        return ''
    return f'Top Author: {publisher.full_name} with {publisher.total_article} published articles.'


def get_top_reviewer():

    top_review =Author.objects.annotate(
        autor_review = Count('reviews_author')
    ).order_by('email').first()
    if top_review is None:
        return ''
    return f'Top Author: {top_review.full_name} with {top_review.autor_review} published reviews.'



def get_latest_article():
    last_article = Article.objects.prefetch_related('authors').annotate(avg_rating=Avg('reviews_article__rating'), num_review=Sum('reviews_article'))
    if last_article is None:
        return ''

    # # author = [a for a in last_article.authors]
    return f"The latest article is: {last_article.title}. Authors: {''}. Reviewed: {last_article.num_reviews} times. Average Rating: {last_article.avg_rating:.2f}."

print(get_latest_article())
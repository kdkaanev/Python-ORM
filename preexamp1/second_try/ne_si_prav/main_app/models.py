from django.core import validators
from django.db import models


# Create your models here.
class Showmen(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[validators.MinLengthValidator(2), ]
    ),
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )
    class Meta:
        abstract = True


class Director(Showmen):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[validators.MinValueValidator(0)]
    )


class Actor(Showmen):

    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    CHOICE_GENRE= (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other')

    )
    title = models.CharField(
        max_length=150,
        validators=[validators.MinLengthValidator(5)]
    )
    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True
    )
    genre = models.CharField(
        max_length=6,
        choices=CHOICE_GENRE,
        default='Other'

    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.0),
            validators.MaxValueValidator(10.0)
        ],
        default=0.0

    )
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='movies_director'
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='movies_actor'
    )
    actors = models.ManyToManyField(to=Actor)
from django.db import models
from django.core import validators

from main_app.managers import DirectorManager


# Create your models here.
class Director(models.Model):
    full_name = models.CharField(
        validators=[
            validators.MinLengthValidator(2),
            validators.MaxLengthValidator(120),
        ]
    )
    birth_date = models.DateField(
        default='1900-01-01'
    )
    nationality = models.CharField(
        default='Unknown',
        validators=[
            validators.MaxLengthValidator(50),
        ]
    )
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[
            validators.MinValueValidator(0),
        ]
    )
    objects = DirectorManager()

    def __str__(self):
        return self.full_name


class Actor(models.Model):
    full_name = models.CharField(
        validators=[
            validators.MinLengthValidator(2),
            validators.MaxLengthValidator(120),
        ]
    )
    birth_date = models.DateField(
        default='1900-01-01'
    )
    nationality = models.CharField(
        default='Unknown',
        validators=[
            validators.MaxLengthValidator(50),
        ]
    )
    is_awarded = models.BooleanField(
        default=False
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )


class Movie(models.Model):
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other'),

    )
    title = models.CharField(
        validators=[
            validators.MinLengthValidator(2),
            validators.MaxLengthValidator(150),
        ]
    )


    release_date = models.DateField()

    storyline = models.TextField(
        blank=True,
        null=True,

    )

    genre = models.CharField(
        choices=GENRE_CHOICES,
        default='Other',
        validators=[
            validators.MaxLengthValidator(6),
        ]
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            validators.MinValueValidator(0.0),
            validators.MaxValueValidator(10.0),
        ]
    )

    is_classic = models.BooleanField(
        default=False
    )

    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='movies',

    )

    starring_actor = models.ForeignKey(
        Actor,
        null=True,
        on_delete=models.SET_NULL,
        related_name='actors',
    )
    actors = models.ManyToManyField(
        to=Actor,

        )


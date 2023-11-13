from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) <
                (self.birth_date.month, self.birth_date.day))
        return age


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class Speciality(models.TextChoices):
        Mammals = 'Mammals'
        Birds = 'Birds'
        Reptiles = 'Reptiles'
        Others = 'Others'

    specialty = models.CharField(max_length=10, choices=Speciality.choices)

    managed_animals = models.ManyToManyField(to=Animal)

    def clean(self):
        super().clean()

        if self.specialty not in self.Speciality:
            raise ValidationError("Specialty must be a valid choice.")


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    def display_info(self):
        return f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}. It makes a noise like '{self.sound}'!{self.__extra_info()}"

    def __extra_info(self):
        info = ''
        if hasattr(self, 'mammal'):
            info = f"Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, 'bird'):
            info = f"Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, 'reptile'):
            info = f"Its scale type is {self.reptile.scale_type}."
        
        return info

    def is_endangered(self):
        return True if self.species in ["Cross River Gorilla", "Orangutan", "Green Turtle"] else False

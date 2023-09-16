from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class recipe(models.Model):
    MEAL_TYPES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snacks', 'Snacks'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES)
    image = models.ImageField(upload_to='recipes_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
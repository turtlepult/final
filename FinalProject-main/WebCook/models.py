from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # Добавьте другие поля по желанию


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    # Добавьте другие поля по желанию


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Добавьте другие поля по желанию

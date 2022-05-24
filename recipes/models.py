from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):  # returna o nome do atributo no admin
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_unit = models.CharField(max_length=20)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=20)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # blank=True, default='' para deixar upar sem imagem
    cover = models.ImageField(
        upload_to='recipes/covers/%y/%m/%d', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f' Пользователь: {self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_cooking = models.TextField()
    image = models.ImageField(upload_to='recipe/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Название блюда: {self.name}'

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:20])}...'


class CategoryRecipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Categories(models.Model):
    recipes = models.ManyToManyField(Recipe)
    categories = models.ForeignKey(CategoryRecipe, on_delete=models.SET_DEFAULT, default='')


from django.db import models
from users.models import Profile


class Plan(models.Model):
    personal_plan = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(
        max_length=200, verbose_name='Plan name', null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    calories = models.DecimalField(
        decimal_places=0, max_digits=4, null=True, blank=False)
    recipes = models.ManyToManyField('Recipe', blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Recipe(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(
        max_length=200, verbose_name='Recipe name', null=True, blank=False)
    ingredients = models.TextField(null=True, blank=False)
    calories = models.DecimalField(
        decimal_places=0, max_digits=4, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    favourites = models.ManyToManyField(
        Profile, blank=True, related_name='favourites')
    # recipe_image = models.ImageField(
    #     null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png'
    #     )
    tag = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return str(self.title)
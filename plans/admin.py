from django.contrib import admin
from .models import Plan, Recipe, Tag

admin.site.register(Plan)
admin.site.register(Recipe)
admin.site.register(Tag)
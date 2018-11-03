from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Slides)
class SlidesAdmin(admin.ModelAdmin):
    list_display = 'title', 'order', 'get_icon'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'category', 'order', 'get_icon'


@admin.register(models.Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = 'name', 'category', 'get_icon'


@admin.register(models.Reviews)
class RevievsAdmin(admin.ModelAdmin):
    list_display = 'client', 'order', 'cut_review', 'get_icon'


@admin.register(models.Stuffing)
class StuffingAdmin(admin.ModelAdmin):
    list_display = 'name', 'order', 'get_icon'



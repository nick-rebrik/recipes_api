from django.contrib import admin

from .models import User, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'image',
        'user',
        'view_count',
    )
    readonly_fields = ('view_count',)
    search_fields = ('title',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'last_name',
    )
    search_fields = ('last_name',)

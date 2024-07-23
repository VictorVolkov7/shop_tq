from django.contrib import admin

from categories.models import Category, SubCategory


# Register Category model in Django admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image',)
    search_fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


# Register SubCategory model in Django admin
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image',)
    search_fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}

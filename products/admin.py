from django.contrib import admin

from products.models import Product


# Register Product model in Django admin
@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_s', 'image_m', 'image_l', 'price',)
    search_fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}

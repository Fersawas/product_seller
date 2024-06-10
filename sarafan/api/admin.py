from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http import HttpRequest
from django.utils.safestring import mark_safe

from products.models import Category, SubCategory, Product
from users.models import ShopCart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'get_image'
    )

    search_fields = ('slug', )

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}"'
                             'style="max-height: 150px">')
        except Exception:
            return None

    get_image.short_description = 'Изображение'



@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'image',
        'category',
        'get_image'
    )
    search_fields = ('slug', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}"'
                         'style="max-height: 150px">')

    get_image.short_description = 'Изображение'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'sub_category',
        'get_image'
    )

    search_fields = ('slug', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.small_image.url}"'
                         'style="max-height: 150px">')

    get_image.short_description = 'Изображение'


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product'
    )
    list_filter = ('user', )

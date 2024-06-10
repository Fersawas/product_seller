from django.db import models
from django.core.validators import MinValueValidator

from products.constants import (MAX_LENGTH, SLUG_LENGTH,
                                PRODUCT_VALIDATOR_MESSAGE)


class Category(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=SLUG_LENGTH,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class SubCategory(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=SLUG_LENGTH,
        verbose_name='Слаг'
    )
    image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Изображение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='sub_categories',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Под-категория'
        verbose_name_plural = 'Под-категории'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Наименование'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH,
        verbose_name='Слаг'
    )
    big_image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Увеличенное изображение'
    )
    medium_image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Среднее изображение'
    )
    small_image = models.ImageField(
        upload_to='media/',
        null=True,
        default=None,
        verbose_name='Уменьшенное изображение'
    )
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        related_name='products',
        verbose_name='Под-категория',
        null=True
    )
    price = models.IntegerField(
        validators=[
            MinValueValidator(
                1,
                message=PRODUCT_VALIDATOR_MESSAGE
            )
        ],
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.title

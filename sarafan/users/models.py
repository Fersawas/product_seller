from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


User = get_user_model()


class ShopCart(models.Model):
    user = models.ForeignKey(
        User, related_name='shopcart',
        on_delete=models.CASCADE,
        verbose_name='Корзина'
    )
    product = models.ForeignKey(
        Product, related_name='shopcart',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )

    class Meta:
        verbose_name: str = 'Корзина'
        verbose_name_plural: str = 'Корзины'

    def __str__(self) -> str:
        return str(self.user.username)

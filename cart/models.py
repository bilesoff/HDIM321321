from django.contrib.auth import get_user_model
from django.db import models

from functools import reduce


class CartGood(models.Model):
    """Сводная таблица, соединяющая товары с корзинами"""
    amount = models.IntegerField(
        verbose_name="Количество"
    )
    cart = models.ForeignKey(
        to='cart.Cart',
        verbose_name='Корзина',
        related_name='goods',
        on_delete=models.CASCADE
    )
    good = models.ForeignKey(
        to='goods.Good',
        verbose_name='Товар',
        related_name=None,
        on_delete=models.CASCADE,
    )

    @property
    def price(self):
        return self.good.price * self.amount

    def __str__(self):
        return f"{str(self.good)} x {self.amount}"


class Cart(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        verbose_name="Пользователь",
        related_name="cart",
        on_delete=models.CASCADE
    )

    services = models.ManyToManyField(
        to='services.Service',
        verbose_name="Услуги",
        related_name=None
    )

    @property
    def is_empty(self):
        return self.services.count() == 0 and self.goods.count() == 0

    @property
    def total_price(self):
        goods_total = reduce(lambda prev, good: prev + good.price, self.goods.all(), 0)
        serivces_total = reduce(lambda prev, service: prev + service.price, self.services.all(), 0)

        return goods_total + serivces_total

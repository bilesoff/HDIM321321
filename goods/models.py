from django.shortcuts import reverse
from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=255
    )
    model = models.CharField(
        verbose_name="Модель",
        max_length=255
    )
    manufacturer = models.CharField(
        verbose_name="Изготовитель",
        max_length=255
    )
    mark = models.CharField(
        verbose_name="Марка",
        max_length=255
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=9,
        decimal_places=2
    )
    article = models.CharField(
        verbose_name="Артикул",
        max_length=255,
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание услуги"
    )
    is_active = models.BooleanField(
        verbose_name="Активный товар",
        default=True
    )

    def __str__(self):
        return f"{self.article} {self.name}"

    def get_absolute_url(self):
        return reverse('catalog_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

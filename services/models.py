from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(
        verbose_name="Наименование услуги",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Описание услуги"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=9,
        decimal_places=2
    )
    good = models.ManyToManyField(
        verbose_name="Товары",
        to='goods.Good',
        related_name='services'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
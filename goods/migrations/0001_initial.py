# Generated by Django 3.2.12 on 2023-06-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Модель')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Изготовитель')),
                ('mark', models.CharField(max_length=255, verbose_name='Марка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('article', models.CharField(max_length=255, unique=True, verbose_name='Артикул')),
                ('description', models.TextField(verbose_name='Описание услуги')),
            ],
        ),
    ]

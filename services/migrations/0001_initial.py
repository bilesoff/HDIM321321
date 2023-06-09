# Generated by Django 3.2.12 on 2023-06-01 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.good', verbose_name='Товар')),
            ],
        ),
    ]

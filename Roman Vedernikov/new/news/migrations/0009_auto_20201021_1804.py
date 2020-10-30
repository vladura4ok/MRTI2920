# Generated by Django 3.1.2 on 2020-10-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20201021_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]

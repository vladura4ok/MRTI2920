# Generated by Django 3.1.2 on 2020-10-21 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0038_auto_20201021_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 23, 52, 13, 315609), verbose_name='Дата публикации'),
        ),
    ]

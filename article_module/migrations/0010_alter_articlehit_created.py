# Generated by Django 4.2.3 on 2023-09-19 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0009_article_hits_article_alter_articlehit_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 20, 0, 23, 28, 171787), verbose_name='تاریخ بازدید'),
        ),
    ]

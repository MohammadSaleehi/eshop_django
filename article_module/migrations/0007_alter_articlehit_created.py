# Generated by Django 4.2.3 on 2023-09-19 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0006_alter_articlehit_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 20, 0, 8, 50, 103163), verbose_name='تاریخ بازدید'),
        ),
    ]

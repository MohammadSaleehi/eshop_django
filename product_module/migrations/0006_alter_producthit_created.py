# Generated by Django 4.2.3 on 2023-09-19 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_product_hits_product_alter_producthit_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 20, 0, 23, 28, 156663), verbose_name='زمان مشاهده'),
        ),
    ]

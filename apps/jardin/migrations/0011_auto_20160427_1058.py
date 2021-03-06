# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 08:58
from __future__ import unicode_literals

import apps.jardin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardin', '0010_auto_20160427_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lopin',
            name='nom',
            field=models.CharField(help_text='Nom du lopin', max_length=50),
        ),
        migrations.AlterField(
            model_name='plante',
            name='espece',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='plante',
            name='image',
            field=models.ImageField(null=True, upload_to=apps.jardin.models.content_file_name_plante),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 08:06
from __future__ import unicode_literals

import apps.jardin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jardin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text='Nom de la ville où se trouve le jardin', max_length=20)),
                ('ville', models.CharField(max_length=20)),
                ('code_postal', models.IntegerField(verbose_name='Code postal')),
                ('rue', models.CharField(max_length=20)),
                ('horaire', models.TextField()),
                ('image', models.ImageField(upload_to=apps.jardin.models.content_file_name)),
                ('description', models.TextField(blank=True, null=True)),
                ('restreint', models.BooleanField()),
            ],
        ),
    ]

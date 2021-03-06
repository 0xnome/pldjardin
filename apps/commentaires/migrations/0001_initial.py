# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jardin', '0002_auto_20160426_1102'),
        ('gensdujardin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentaireJardin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('jardin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jardin.Jardin')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gensdujardin.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireLopin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lopin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jardin.Lopin')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gensdujardin.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='CommentairePlante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('plante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jardin.Plante')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gensdujardin.Utilisateur')),
            ],
        ),
    ]

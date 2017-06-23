# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('dcmt_author_1', models.CharField(max_length=40)),
                ('dcmt_author_2', models.CharField(default='', max_length=40)),
                ('dcmt_author_3', models.CharField(default='', max_length=40)),
                ('dcmt_author_4', models.CharField(default='', max_length=40)),
                ('dcmt_author_5', models.CharField(default='', max_length=40)),
                ('dcmt_author_6', models.CharField(default='', max_length=40)),
                ('dcmt_author_7', models.CharField(default='', max_length=40)),
                ('dcmt_author_8', models.CharField(default='', max_length=40)),
                ('year', models.IntegerField()),
                ('link', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('ART', 'article'), ('CPR', 'conference proceeding'), ('MNG', 'monography'), ('PPR', 'preprint'), ('OTH', 'other')], default='ART', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('patronymic', models.CharField(max_length=40)),
                ('family_name', models.CharField(max_length=40)),
                ('degree', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('photo', models.CharField(max_length=256)),
            ],
        ),
    ]

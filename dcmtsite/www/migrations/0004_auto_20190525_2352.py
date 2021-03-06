# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_person_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='link',
            new_name='download_link',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_1',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_2',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_3',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_4',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_5',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_6',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_7',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='dcmt_author_8',
        ),
        migrations.AddField(
            model_name='paper',
            name='abs_link',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='paper',
            name='authors',
            field=models.CharField(default='T.A. TestAuthor', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='journal',
            field=models.CharField(default='TestJournal, num. 1, vol. 1, p. 1', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='rinc_link',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='paper',
            name='scopus_link',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='paper',
            name='wos_link',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]

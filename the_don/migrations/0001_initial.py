# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True)),
                ('facebook', models.URLField(max_length=255, blank=True)),
                ('instagram', models.URLField(max_length=255, blank=True)),
                ('twitter', models.URLField(max_length=255, blank=True)),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]

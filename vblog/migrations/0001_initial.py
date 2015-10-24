# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True)),
                ('iframe_src', models.CharField(max_length=255)),
                ('vimeo_page', models.URLField(max_length=255, blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('HTM', models.CharField(max_length=100, blank=True)),
                ('gallery_image_1', models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True)),
                ('gallery_image_2', models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True)),
                ('gallery_image_3', models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True)),
                ('pubdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

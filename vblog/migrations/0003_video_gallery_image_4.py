# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0002_video_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='gallery_image_4',
            field=models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True),
        ),
    ]

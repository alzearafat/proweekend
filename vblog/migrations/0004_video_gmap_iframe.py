# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0003_video_gallery_image_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='gmap_iframe',
            field=models.TextField(default=datetime.datetime(2015, 10, 25, 13, 29, 39, 452699, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

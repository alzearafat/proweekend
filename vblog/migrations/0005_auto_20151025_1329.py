# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0004_video_gmap_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='gmap_iframe',
            field=models.TextField(blank=True),
        ),
    ]

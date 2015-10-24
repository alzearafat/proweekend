# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='location',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]

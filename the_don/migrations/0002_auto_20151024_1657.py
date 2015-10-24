# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_don', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='card_image',
            new_name='card_image_header',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_picture_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='big_picture',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]

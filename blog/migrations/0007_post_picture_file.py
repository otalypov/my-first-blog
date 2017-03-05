# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170303_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture_file',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

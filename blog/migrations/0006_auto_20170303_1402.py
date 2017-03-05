# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170302_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='post',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-08 01:13

import blacklist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='places',
            field=models.JSONField(default=blacklist.models.jsonfield_default),
        ),
    ]
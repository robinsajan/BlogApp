# Generated by Django 3.2.4 on 2021-07-14 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20210714_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 22, 1, 56274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 22, 1, 57313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 22, 1, 57313, tzinfo=utc)),
        ),
    ]

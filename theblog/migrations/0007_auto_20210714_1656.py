# Generated by Django 3.2.4 on 2021-07-14 11:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210714_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 11, 26, 24, 669734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 11, 26, 24, 673419, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 11, 26, 24, 674415, tzinfo=utc)),
        ),
    ]
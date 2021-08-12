# Generated by Django 3.2.4 on 2021-07-14 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_auto_20210714_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='overview',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec luctus sem interdum, faucibus sem id, mollis mauris. Quisque tempor iaculis tempor. Nam at ligula lacus. Morbi consequat condimentum arcu, laoreet dignissim velit interdum id. Donec vel eleifend nunc. Morbi tincidunt feugiat justo eu luctus. '),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 21, 14, 176022, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 21, 14, 177018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 14, 21, 14, 177018, tzinfo=utc)),
        ),
    ]
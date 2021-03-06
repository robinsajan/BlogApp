# Generated by Django 3.2.4 on 2021-07-14 12:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_auto_20210714_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 12, 5, 52, 887659, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theblog.tags'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 12, 5, 52, 887659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 12, 5, 52, 887659, tzinfo=utc)),
        ),
    ]

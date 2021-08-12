# Generated by Django 3.2.4 on 2021-07-14 15:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0017_auto_20210714_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 15, 2, 31, 254507, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 15, 2, 31, 255504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 15, 2, 31, 256502, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('about_me', models.TextField()),
                ('phone_no', models.CharField(max_length=10)),
                ('instagram_url', models.URLField(blank=True, default='', null=True)),
                ('linkeden_url', models.URLField(blank=True, default='', null=True)),
                ('twitter_url', models.URLField(blank=True, default='', null=True)),
                ('pitrest_url', models.URLField(blank=True, default='', null=True)),
                ('dribble_url', models.URLField(blank=True, default='', null=True)),
                ('website_url', models.URLField(blank=True, default='', null=True)),
                ('github_url', models.URLField(blank=True, default='', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
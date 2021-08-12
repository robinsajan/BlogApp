# Generated by Django 3.2.4 on 2021-07-12 12:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 7, 12, 12, 57, 46, 888493, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 7, 12, 12, 57, 46, 889494, tzinfo=utc))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theblog.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('context', models.TextField()),
                ('image', models.ImageField(blank=True, default='images/img3.png', null=True, upload_to='tag_title/')),
                ('tag_bg_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2021, 7, 12, 12, 57, 46, 890489, tzinfo=utc))),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theblog.comments')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theblog.tags'),
        ),
    ]
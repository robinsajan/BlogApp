# Generated by Django 3.2.4 on 2021-07-18 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0027_comments_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]

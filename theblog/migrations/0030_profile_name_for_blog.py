# Generated by Django 3.2.4 on 2021-07-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0029_auto_20210718_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name_for_blog',
            field=models.CharField(default='Tales Of Wasseypur', max_length=150),
        ),
    ]

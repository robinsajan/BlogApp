# Generated by Django 3.2.4 on 2021-07-18 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0023_alter_comments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

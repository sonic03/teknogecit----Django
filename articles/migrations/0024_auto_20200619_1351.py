# Generated by Django 3.0.7 on 2020-06-19 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0023_auto_20200619_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_author',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
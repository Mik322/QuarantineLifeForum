# Generated by Django 3.0.5 on 2020-04-20 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='followers',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-20 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200420_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 13, 56, 14, 599398, tzinfo=utc), verbose_name='Publication date'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-29 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 29, 11, 13, 18, 119791, tzinfo=utc)),
        ),
    ]

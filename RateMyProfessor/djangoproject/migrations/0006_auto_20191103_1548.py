# Generated by Django 2.2.6 on 2019-11-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0005_auto_20191103_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-22 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]

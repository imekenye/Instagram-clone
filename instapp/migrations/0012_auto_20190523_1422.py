# Generated by Django 2.2.1 on 2019-05-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0011_auto_20190523_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
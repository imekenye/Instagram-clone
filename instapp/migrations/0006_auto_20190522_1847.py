# Generated by Django 2.2.1 on 2019-05-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0005_image_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='post_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]

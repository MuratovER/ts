# Generated by Django 3.1.6 on 2021-04-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0030_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='image_of_user'),
        ),
    ]

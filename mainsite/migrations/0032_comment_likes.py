# Generated by Django 3.1.6 on 2021-04-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0031_auto_20210407_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default='0'),
        ),
    ]
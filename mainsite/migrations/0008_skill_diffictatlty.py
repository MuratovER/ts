# Generated by Django 2.2.10 on 2020-07-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20200716_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='diffictatlty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='difficulty', to='mainsite.Difficulty'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]

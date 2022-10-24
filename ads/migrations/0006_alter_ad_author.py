# Generated by Django 4.1.2 on 2022-10-24 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_location_lat_alter_location_lng'),
        ('ads', '0005_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='user.user', verbose_name='Автор'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_map_on_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='maps/'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20200411_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='id_on_map',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='on_map',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='xcor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='ycor',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 3.1.5 on 2022-03-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20220315_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='cenaB',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='cenaE',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 3.2 on 2023-08-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellercounter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tellercounter',
            name='amt_cash',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
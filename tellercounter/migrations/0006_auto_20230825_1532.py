# Generated by Django 3.2 on 2023-08-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellercounter', '0005_tellercounter_pan_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashcontributor',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='chequecontributor',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='draftcontributor',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='kindcontributor',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
# Generated by Django 3.2 on 2023-08-26 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tellercounter', '0008_auto_20230826_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='draftcontributor',
            old_name='bank_cheque',
            new_name='bank_draft',
        ),
    ]

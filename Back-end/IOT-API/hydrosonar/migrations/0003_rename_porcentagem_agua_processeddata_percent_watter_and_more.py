# Generated by Django 4.2.5 on 2023-11-25 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydrosonar', '0002_processeddata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processeddata',
            old_name='porcentagem_agua',
            new_name='percent_water',
        ),
        migrations.RenameField(
            model_name='processeddata',
            old_name='valvula_ativa',
            new_name='valve_state',
        ),
        migrations.RenameField(
            model_name='processeddata',
            old_name='volume_litros',
            new_name='volume_liters',
        ),
    ]

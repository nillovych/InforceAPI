# Generated by Django 4.1.2 on 2022-10-15 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestrauntApp', '0003_alter_restraunts_restrauntmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restraunts',
            name='RestrauntMenu',
        ),
    ]

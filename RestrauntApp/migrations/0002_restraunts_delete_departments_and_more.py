# Generated by Django 4.1.2 on 2022-10-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestrauntApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restraunts',
            fields=[
                ('RestrauntId', models.AutoField(primary_key=True, serialize=False)),
                ('RestrauntName', models.CharField(max_length=500)),
                ('RestrauntMenu', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='DateOfJoining',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='PhotoFileName',
        ),
        migrations.AddField(
            model_name='employees',
            name='Vote',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

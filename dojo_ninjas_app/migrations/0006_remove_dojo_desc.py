# Generated by Django 3.2.7 on 2021-10-08 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0005_dojo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
    ]

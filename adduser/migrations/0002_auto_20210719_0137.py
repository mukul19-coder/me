# Generated by Django 2.1.15 on 2021-07-18 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adduser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_transport',
            new_name='client',
        ),
        migrations.RenameModel(
            old_name='add_client',
            new_name='transport',
        ),
    ]

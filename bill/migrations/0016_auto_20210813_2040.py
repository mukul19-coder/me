# Generated by Django 2.1.15 on 2021-08-13 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0015_auto_20210813_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='temp',
            name='gst',
        ),
    ]

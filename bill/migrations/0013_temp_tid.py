# Generated by Django 2.1.15 on 2021-08-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0012_auto_20210813_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp',
            name='tid',
            field=models.IntegerField(default=1, max_length=2),
        ),
    ]

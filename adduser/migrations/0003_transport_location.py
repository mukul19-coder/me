# Generated by Django 2.1.15 on 2021-07-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adduser', '0002_auto_20210719_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

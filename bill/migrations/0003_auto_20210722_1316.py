# Generated by Django 2.1.15 on 2021-07-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_auto_20210722_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# Generated by Django 2.1.15 on 2021-08-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0023_auto_20210814_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='ewaybill',
            field=models.CharField(blank=True, default='---------', max_length=100),
        ),
    ]
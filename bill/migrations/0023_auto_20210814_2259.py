# Generated by Django 2.1.15 on 2021-08-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0022_auto_20210814_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

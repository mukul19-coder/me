# Generated by Django 2.1.15 on 2021-08-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0011_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='gst',
            field=models.CharField(choices=[('I-GST', 'I-GST'), ('C-GST & S-GST', 'C-GST & S-GST')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='temp',
            name='payment',
            field=models.CharField(choices=[('CASH', 'CASH'), ('NEFT', 'NEFT')], default=None, max_length=100),
        ),
    ]
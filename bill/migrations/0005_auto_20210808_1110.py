# Generated by Django 2.1.15 on 2021-08-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0004_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='img',
        ),
        migrations.AddField(
            model_name='bill',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]
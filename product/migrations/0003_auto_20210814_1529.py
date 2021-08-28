# Generated by Django 2.1.15 on 2021-08-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_mtr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mtr',
        ),
        migrations.AddField(
            model_name='product',
            name='hsn',
            field=models.CharField(choices=[('5806', '5806'), ('6002', '6002')], default='5806', max_length=100),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-13 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200513_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='line_item_name',
        ),
    ]
# Generated by Django 3.0.6 on 2020-06-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20200531_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradditionalinfo',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
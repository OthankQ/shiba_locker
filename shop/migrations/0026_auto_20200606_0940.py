# Generated by Django 3.0.6 on 2020-06-06 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200606_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passcode',
            old_name='passcode',
            new_name='pass_code',
        ),
        migrations.RenameField(
            model_name='passcode',
            old_name='text_passcode',
            new_name='text_pass_code',
        ),
    ]

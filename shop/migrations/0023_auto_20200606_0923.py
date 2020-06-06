# Generated by Django 3.0.6 on 2020-06-06 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0022_useradditionalinfo_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradditionalinfo',
            name='password_resetting',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='PassCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passcode', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
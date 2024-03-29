# Generated by Django 3.0.6 on 2020-05-16 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='invoice creation date')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('cart', 'cart'), ('pending', 'pending'), ('shipped', 'shipped'), ('fulfilled', 'fulfilled')], default='cart', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image_id', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdditionalInfo',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('line_item', models.AutoField(primary_key=True, serialize=False)),
                ('line_item_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('quantity', models.IntegerField(default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Invoice')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.InvoiceStatus'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

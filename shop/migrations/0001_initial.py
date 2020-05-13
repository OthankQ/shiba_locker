# Generated by Django 3.0.6 on 2020-05-13 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='invoice creation date')),
                ('status', models.CharField(max_length=255)),
                ('etc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image_id', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('etc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('line_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('line_item_name', models.CharField(max_length=255)),
                ('line_item_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('quantity', models.IntegerField()),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Invoice')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
        ),
    ]

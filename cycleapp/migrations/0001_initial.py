# Generated by Django 3.2.7 on 2022-03-17 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_name', models.CharField(max_length=100)),
                ('bike_image', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('mtb', 'Mtb'), ('road', 'Road'), ('hybrid', 'Hybrid'), ('fatbike', 'Fatbike'), ('electric_bike', 'Electric'), ('other', 'Other')], default='mtb', max_length=50)),
                ('description', models.TextField()),
                ('stock', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('date_sell', models.DateField(auto_now=True)),
                ('delivery_time', models.PositiveIntegerField()),
                ('total_sold', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_payment', models.PositiveIntegerField(blank=True, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,10}$')])),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('paypal', 'PayPal'), ('upipay', 'UpiPay'), ('cashpay', 'CashPay')], default='cashpay', max_length=100)),
                ('order_date', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_date', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_in_Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_payment', models.PositiveIntegerField(blank=True, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{0,10}$')])),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('paypal', 'PayPal'), ('upipay', 'UpiPay'), ('cashpay', 'CashPay')], default='cashpay', max_length=100)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_progress_cycles', to='cycleapp.cycle')),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-09 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='shipping.shippingprovider')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_min', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight_max', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='shipping.shippingoption')),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='activity_type',
            field=models.CharField(choices=[('login', 'login'), ('purchase', 'Purchase'), ('view_product', 'View Product'), ('search', 'Search')], max_length=255),
        ),
    ]
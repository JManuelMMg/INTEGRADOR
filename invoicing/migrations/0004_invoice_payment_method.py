# Generated by Django 5.2.1 on 2025-05-31 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0003_auto_20250530_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Efectivo'), ('card', 'Tarjeta'), ('transfer', 'Transferencia')], max_length=20, null=True),
        ),
    ]

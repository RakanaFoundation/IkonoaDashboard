# Generated by Django 3.1.5 on 2021-04-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0019_auto_20210411_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paymentMethod',
        ),
        migrations.RemoveField(
            model_name='spending',
            name='paymentMethod',
        ),
        migrations.AddField(
            model_name='payment',
            name='expiryDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymethod',
            field=models.CharField(choices=[('CASH', 'Cash'), ('GIRO', 'Giro'), ('CARD', 'Card')], default='CASH', max_length=4),
        ),
        migrations.AddField(
            model_name='spending',
            name='expiryDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spending',
            name='paymethod',
            field=models.CharField(choices=[('CASH', 'Cash'), ('GIRO', 'Giro'), ('CARD', 'Card')], default='CASH', max_length=4),
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]

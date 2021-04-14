# Generated by Django 3.1.5 on 2021-03-27 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0013_auto_20210327_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faktur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(choices=[('CASH', 'Cash'), ('GIRO', 'Giro'), ('CARD', 'Card')], default='CASH', max_length=4)),
                ('expiryDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('detail', models.CharField(max_length=200)),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.paymentmethod')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFaktur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('faktur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.faktur')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.product')),
            ],
        ),
        migrations.AddField(
            model_name='faktur',
            name='spending',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.spending', unique=True),
        ),
        migrations.AddField(
            model_name='faktur',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.supplier'),
        ),
    ]
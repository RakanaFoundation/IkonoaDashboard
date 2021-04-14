# Generated by Django 3.1.5 on 2021-04-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0026_auto_20210414_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faktur',
            name='cabang',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='cabang',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang'),
        ),
        migrations.CreateModel(
            name='PusatProductInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0)),
                ('reminderStockAt', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.product')),
            ],
        ),
    ]

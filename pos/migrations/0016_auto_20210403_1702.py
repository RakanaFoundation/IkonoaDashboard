# Generated by Django 3.1.5 on 2021-04-03 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pos.financemodels


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pos', '0015_auto_20210329_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(blank=True, null=True)),
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('detail', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.paymentmethod')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier', models.CharField(max_length=200)),
                ('trackingId', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='spending',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SalesTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_id', models.CharField(default='', editable=False, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.employee')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.payment')),
            ],
        ),
        migrations.CreateModel(
            name='OrderSent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.order')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.order')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('REJECT', 'Rejected'), ('APPROVE', 'Approved'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('detail', models.CharField(max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('REJECT', 'Rejected'), ('APPROVE', 'Approved'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('detail', models.CharField(max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.order')),
            ],
        ),
    ]
# Generated by Django 3.1.5 on 2021-04-13 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0021_salestransaction_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabang',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='dateFrom',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='dateTo',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='NotaCabang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notanumber', models.IntegerField(default=1)),
                ('cabang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang')),
            ],
        ),
    ]

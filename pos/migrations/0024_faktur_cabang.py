# Generated by Django 3.1.5 on 2021-04-13 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0023_auto_20210413_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='faktur',
            name='cabang',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='pos.cabang'),
            preserve_default=False,
        ),
    ]

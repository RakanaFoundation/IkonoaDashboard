# Generated by Django 3.1.5 on 2021-03-27 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0012_auto_20210327_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pos.maincategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pos.promotion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCategoryOne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pos.subcategoryone'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCategoryTwo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pos.subcategorytwo'),
        ),
    ]

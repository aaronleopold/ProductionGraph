# Generated by Django 3.0.6 on 2020-06-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200605_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='indirect_labor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='indirect_wages',
            field=models.FloatField(default=0),
        ),
    ]

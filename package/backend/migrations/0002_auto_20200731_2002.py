# Generated by Django 3.0.7 on 2020-07-31 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='measurement',
            field=models.CharField(default='Unit', max_length=40),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('measurement', models.CharField(max_length=40)),
                ('real_price', models.FloatField()),
                ('direct_labor', models.FloatField()),
                ('direct_wages', models.FloatField()),
                ('indirect_wages', models.FloatField(default=0)),
                ('indirect_labor', models.FloatField(default=0)),
                ('history_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.HistoryPoint')),
            ],
        ),
        migrations.CreateModel(
            name='DependencyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependent_id', models.IntegerField()),
                ('dependency_id', models.IntegerField()),
                ('quantity', models.FloatField()),
                ('history_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.HistoryPoint')),
            ],
        ),
        migrations.CreateModel(
            name='DependencyCycleError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
            ],
        ),
    ]

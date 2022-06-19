# Generated by Django 3.0.8 on 2020-10-08 03:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=900)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=100)),
                ('batch_no', models.CharField(max_length=25)),
                ('cost', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('mfg', models.DateField()),
                ('exp', models.DateField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_set', to='home.Supplier')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
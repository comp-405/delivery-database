# Generated by Django 2.2 on 2019-04-26 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('ssn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('tip', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='delivery.Driver')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='delivery.Vehicle')),
            ],
        ),
    ]

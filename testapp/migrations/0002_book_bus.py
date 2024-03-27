# Generated by Django 4.0 on 2024-03-27 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('borrow_count', models.IntegerField(default=0)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameBus', models.CharField(max_length=255)),
                ('content', models.TextField(default='')),
                ('price', models.PositiveSmallIntegerField(default=1)),
                ('year', models.PositiveSmallIntegerField(default=1800)),
                ('imgCar', models.ImageField(blank=True, null=True, upload_to='mediacar')),
            ],
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201203_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_cu',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time_cu',
            field=models.CharField(max_length=100),
        ),
    ]

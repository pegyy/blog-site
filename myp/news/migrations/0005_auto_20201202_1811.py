# Generated by Django 3.1.3 on 2020-12-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201126_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_txt',
            field=models.TextField(default='-', max_length=300),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20201209_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text2',
            field=models.TextField(default='-', max_length=3000),
        ),
        migrations.AddField(
            model_name='news',
            name='text3',
            field=models.TextField(default='-', max_length=3000),
        ),
    ]

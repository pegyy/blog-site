# Generated by Django 3.1.3 on 2020-12-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='emailcu',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='namecu',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='textcu',
            field=models.TextField(max_length=100),
        ),
    ]

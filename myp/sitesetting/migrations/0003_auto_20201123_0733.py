# Generated by Django 3.1.3 on 2020-11-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0002_auto_20201122_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='tag',
            field=models.TextField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='banner1',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='banner1url',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='insta',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='logo',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='logourl',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='sitename',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='tlg',
            field=models.CharField(max_length=100),
        ),
    ]

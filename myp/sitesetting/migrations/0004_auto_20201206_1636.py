# Generated by Django 3.1.3 on 2020-12-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0003_auto_20201123_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='bio',
            field=models.TextField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='name',
            field=models.TextField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.TextField(default='-', max_length=100),
        ),
    ]
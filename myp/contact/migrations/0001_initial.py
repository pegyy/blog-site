# Generated by Django 3.1.3 on 2020-12-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecu', models.TextField(default='-', max_length=100)),
                ('emailcu', models.TextField(default='-', max_length=100)),
                ('textcu', models.TextField(default='-', max_length=100)),
                ('time_cu', models.CharField(default='-', max_length=100)),
                ('date_cu', models.CharField(default='-', max_length=100)),
                ('texta', models.TextField(default='-', max_length=200)),
            ],
        ),
    ]

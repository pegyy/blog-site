# Generated by Django 3.1.3 on 2020-11-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='-', max_length=100)),
                ('upass', models.TextField(default='-', max_length=100)),
                ('username', models.TextField(default='-', max_length=100)),
                ('email', models.TextField(default='-', max_length=100)),
                ('phone', models.TextField(default='-', max_length=100)),
                ('address', models.TextField(default='-', max_length=100)),
                ('pic', models.TextField(default='-', max_length=100)),
                ('picurl', models.TextField(default='-', max_length=100)),
                ('pip', models.TextField(default='-', max_length=100)),
                ('number', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_pemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_title',
            field=models.TextField(default='-', max_length=200),
        ),
    ]

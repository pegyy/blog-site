# Generated by Django 3.1.3 on 2020-12-17 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_contact_newsletters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Newsletters',
            new_name='newsletters',
        ),
    ]

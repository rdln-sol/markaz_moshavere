# Generated by Django 4.2.8 on 2023-12-28 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conditions',
            new_name='Condition',
        ),
    ]
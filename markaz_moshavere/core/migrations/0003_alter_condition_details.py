# Generated by Django 4.2.8 on 2024-01-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_dossier_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='details',
            field=models.TextField(max_length=2047),
        ),
    ]

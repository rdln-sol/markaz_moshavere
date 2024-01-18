# Generated by Django 4.2.8 on 2024-01-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'مرد'), (2, 'زن')], default=1),
        ),
    ]
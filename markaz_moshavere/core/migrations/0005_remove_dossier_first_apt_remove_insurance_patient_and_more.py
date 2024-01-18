# Generated by Django 4.2.8 on 2024-01-07 16:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_condition_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossier',
            name='first_apt',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='interventions',
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='psychologist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.psychologist'),
        ),
        migrations.AddField(
            model_name='patient_conditions',
            name='diagnosis_date',
            field=models.CharField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='patient_conditions',
            name='psychologist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.psychologist'),
        ),
        migrations.AddField(
            model_name='patient_conditions',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'حل شده'), (2, 'تحت درمان'), (3, 'درگیر')], default=3),
        ),
        migrations.AddField(
            model_name='treatment_plan',
            name='interventions',
            field=models.CharField(default='', max_length=100),
        ),
    ]

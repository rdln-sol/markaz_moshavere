# Generated by Django 4.2.8 on 2024-01-07 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_dossier_first_apt_remove_insurance_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='psychologist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.psychologist'),
        ),
        migrations.AlterField(
            model_name='patient_conditions',
            name='psychologist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.psychologist'),
        ),
        migrations.AlterField(
            model_name='treatment_plan',
            name='interventions',
            field=models.CharField(max_length=100),
        ),
    ]
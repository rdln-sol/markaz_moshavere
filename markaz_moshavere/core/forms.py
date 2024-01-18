from django import forms
from .models import *

class Psychologist_form(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = "__all__"

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class Appointment_form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

class Profit_form(forms.ModelForm):
    class Meta:
        model = Profit
        fields = "__all__"

class Condition_form(forms.ModelForm):
    class Meta:
        model = Condition
        fields = "__all__"

class patient_conditions_form(forms.ModelForm):
    class Meta:
        model = patient_conditions
        fields = "__all__"

class Dossier_form(forms.ModelForm):
    class Meta:
        model = Dossier
        fields = "__all__"

class Treatment_Plan_form(forms.ModelForm):
    class Meta:
        model = Treatment_Plan
        fields = "__all__"

class Medication_form(forms.ModelForm):
    class Meta:
        model = Medication
        fields = "__all__"

class Insurance_form(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = "__all__"

class patient_insurance_form(forms.ModelForm):
    class Meta:
        model = patient_insurance
        fields = "__all__"
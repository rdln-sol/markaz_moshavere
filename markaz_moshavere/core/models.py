from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from .manager import ReceptionManager

# Create your models here.

class Patient(models.Model):
    f_name = models.CharField(max_length=255, blank=False, null=False)
    l_name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"



TIME_CHOICES = (
    ("3:00 PM", "3:00 PM-4:00 PM"),
    ("4:00 PM", "4:00 PM-5:00 PM"),
    ("5:00 PM", "5:00 PM-6:00 PM"),
    ("6:00 PM", "6:00 PM-7:00 PM"),
    ("7:00 PM", "7:00 PM-8:00 PM"),
)


class Reception(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, primary_key=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = ReceptionManager()

class Psychologist(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    specialty_field = models.CharField(max_length=255)
    detail = models.TextField(max_length=2047, null=True, blank=True)
    receptionist = models.ForeignKey(Reception, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/image', null=True, blank=True)
    photo_logo = models.ImageField(upload_to='media/image', null=True, blank=True)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
    

class Appointment(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.CharField(default=date.today)
    start_time = models.CharField(choices=TIME_CHOICES, max_length=10, default="3 PM")
    payment_amount = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)

    class Meta:
        unique_together = ['psychologist', 'patient', 'date', 'start_time']
    

class Profit(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    date = models.CharField(default=date.today)

class Condition(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=2047)

    def __str__(self):
        return self.name
    

class patient_conditions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    conditions = models.ForeignKey(Condition, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField(choices=(
        (1, 'حل شده'),
        (2, 'تحت درمان'),
        (3, 'درگیر')
    ), default=3)
    diagnosis_date = models.CharField(default=date.today)


class Dossier(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    birth_date = models.CharField(default=date.today)
    job = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.PositiveSmallIntegerField(
        choices = (
            (1, 'مجرد'),
            (2, 'نامزد'),
            (3, 'عقد'),
            (4, 'متأهل'),
            (5, 'ازدواج موقت'),
            (6, 'تعدد زوجات'),
            (7, 'ازدواج مجدد'),
            (8, 'متارکه'),
            (9, 'مطلقه'),
            (10, 'بیوه')
        )
    )
    educational_status = models.PositiveSmallIntegerField(
        choices = (
            (1, '(سنین بالا)بی سواد'),
            (2, 'زیر سن مدرسه'),
            (3, 'پیش دبستانی'),
            (5, 'ابتدایی(دانش آموز)'),
            (6, '(دانش آموز)راهنمایی'),
            (7, '(دانش آموز)دبیرستان'),
            (8, 'ابتدایی(ترک تحصیل)'),
            (9, 'راهنمایی(ترک تحصیل)'),
            (10, 'دبیرستان(ترک تحصیل)'),
            (11, 'دیپلم و پیش دانشگاهی'),
            (12, 'دارای مدرک دانشگاهی'),
            (13, 'دانشجو'),
            (14, 'حوزوی')
        )
    )

    gender = models.PositiveSmallIntegerField(
        choices = (
            (1, 'مرد'),
            (2, 'زن')
        ),
        default = 1
    )
    class Meta:
        unique_together=['patient', 'psychologist']

    def __str__(self):
        return f"{self.patient}, {self.psychologist}"
    

class Treatment_Plan(models.Model):
    name = models.CharField(max_length=255)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100)
    interventions = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Medication(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=63)
    frequency = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255, default=datetime.now)
    end_time = models.CharField(max_length=255)
    

class Insurance(models.Model):
    company = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class patient_insurance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
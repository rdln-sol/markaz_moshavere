
from django.db import models
from multiselectfield import MultiSelectField
from datetime import date, datetime

# Create your models here.

class Patient(models.Model):
    f_name = models.CharField(max_length=255, blank=False, null=False)
    l_name = models.CharField(max_length=255, blank=False, null=False)
    birth_date = models.DateField()
    job = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    referal_source = MultiSelectField(choices = (
            (1, 'جراید'),
            (2, 'سایر مراجعان'),
            (3, 'تلویزیون'),
            (4, 'رادیو'),
            (5, 'پوستر'),
            (6, 'بروشور'),
            (7, 'تابلو های تبلیغاتی (بیلبورد)'),
            (8, 'اطلاع رسانی تلفنی (118)'),
            (9, 'خط 148 (صدای مشاور)'),
            (10, 'سایر')
        ),
        max_choices = 10, max_length=10
    )


class Psychologist(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    detail = models.TextField(max_length=2056)
    avail = MultiSelectField(choices = (
        (0, 'شنبه'),
        (1, 'یکشنبه'),
        (2, 'دوشنبه'),
        (3, 'سه‌شنبه'),
        (4, 'چهارشنبه'),
        (5, 'پنجشنبه'),
    ))
    specialty_field = models.CharField(max_length=255)


TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Appointment(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    start_time = models.CharField(choices=TIME_CHOICES, max_length=10, default="3 PM")
    payment_method = models.PositiveSmallIntegerField(choices = (
        (1, 'نقدی'),
        (2,'کارت')
    ))
    available_status = models.BooleanField(default=True)

class treatment_plan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100)
    interventions = models.CharField(max_length=100)

class Reception(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)


class Profit(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    amount = models.DecimalField()
    date = models.DateField(default=date.today())

class Conditions(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ManyToManyField(Patient, on_delete=models.CASCADE)

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    medication_name = models.CharField(max_field=100)
    dosage = models.CharField(max_length=63)
    frequency = models.CharField(max_length=255)
    start_time = models.DateField(default=datetime.now)
    end_time = models.DateField()

class Dossier(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    first_apt = models.DateField(default=date.today)
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
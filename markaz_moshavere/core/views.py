from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.apps import apps
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html', context={
        'Psychologist':Psychologist.objects.all()
    })

def login_reception(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        reception = authenticate(request, phone_number=phone_number, password=password)
        if reception is not None:
            login(request, reception)
            return HttpResponseRedirect(reverse('dash', args=('Psychologist',)))
        return render(request, 'login.html', context={
            'message': 'شماره کاربری یا رمز عبور اشتباه است'
        })
    return render(request, 'login.html')

def logout_reception(request):
    logout(request)
    return redirect('index')

STATIC_CODE = "2525"
times_list = [
    ["3:00 PM", "3:00 PM-4:00 PM"],
    ["4:00 PM", "4:00 PM-5:00 PM"],
    ["5:00 PM", "5:00 PM-6:00 PM"],
    ["6:00 PM", "6:00 PM-7:00 PM"],
    ["7:00 PM", "7:00 PM-8:00 PM"],
]

def book(request):
    if request.method == 'POST':
        try:
            psychologist = request.POST.get('psych')
            date = request.POST.get('date')
            time = request.POST.get('time')
            first_name = request.POST.get('f_name')
            last_name = request.POST.get('l_name')
            phone_number = request.POST.get('phone_number')
            code = request.POST.get('code')
        except:
            return render(request, 'appointment.html', context={
                'psychos': Psychologist.objects.all(),
                'times': times_list,
                'message': 'فیلد هارا به درستی وارد کنید'
            })

        print(psychologist)
        psych = Psychologist.objects.get(id=psychologist)

        if not Appointment.objects.filter(
            psychologist = psych,
            date = date,
            start_time = time
        ).exists():
            if first_name and last_name and phone_number:
                patient = Patient.objects.get_or_create(
                f_name=first_name, 
                l_name=last_name, 
                phone_number=phone_number
                )[0]
            else:
                return render(request, 'appointment.html', context={
                    'psychos': Psychologist.objects.all(),
                    'times': times_list,
                    'message': 'kir'
                })
            app = Appointment.objects.create(
                psychologist = psych,
                patient = patient,
                date = date,
                start_time = time
            )
        else:
            return render(request, 'appointment.html', context={
                'psychos': Psychologist.objects.all(),
                'times': times_list,
                'message': 'زمان انتخاب شده پر میباشد'
            })
        if app is not None:
            if STATIC_CODE == code:
                return render(request, 'approved.html', context={
                    'app': app
                })
            return render(request, 'appointment.html', context={
                'psychos': Psychologist.objects.all(),
                'times': times_list,
                'message': 'کد وارد شده اشتباه میباشد'
            })
        return render(request, 'appointment.html', context={
            'psychos': Psychologist.objects.all(),
            'times': times_list,
            'message': 'اطلاعات وارد شده اشتباه میباشد'
        })


    return render(request, 'appointment.html', context={
        'psychos': Psychologist.objects.all(),
        'times': times_list
    })

@login_required
def dashboard_view(request, page):

    model = apps.get_model('core', f'{page}')
    instances_list = model.objects.all().values()
    pages = request.GET.get('page', 1)

    paginator = Paginator(instances_list, 6)
    try:
        instances = paginator.page(pages)
    except PageNotAnInteger:
        instances = paginator.page(pages)
    except EmptyPage:
        instances = paginator.page(paginator.num_pages)
    
    curr_url = resolve(request.path_info).kwargs.get('page')
    if curr_url == 'Psychologist':
        form = Psychologist_form
        page_name = 'مشاوران'
    elif curr_url == 'Patient':
        form = Patient_form
        page_name = 'مراجعین'
    elif curr_url == 'Appointment':
        form = Appointment_form
        page_name = 'نوبت ها'
    elif curr_url == 'Profit':
        form = Profit_form
        page_name = 'درآمد'
    elif curr_url == 'Condition':
        form = Condition_form
        page_name = 'تشخیص'
    elif curr_url == 'Dossier':
        form = Dossier_form
        page_name = 'پرونده ها'
    elif curr_url == 'Treatment_Plan':
        form = Treatment_Plan_form
        page_name = 'برنامه های درمانی'
    elif curr_url == 'Medication':
        form = Medication_form
        page_name = 'برنامه های دارویی'
    elif curr_url == 'patient_conditions':
        form = patient_conditions_form
        page_name = 'تشخیص مراجعین'
    elif curr_url == 'patient_insurance':
        form = patient_insurance_form
        page_name = 'بیمه بیماران'
    else:
        form = Insurance_form
        page_name = 'بیمه'

    fields = [x.name for x in list(model._meta.fields)]

    if request.method == 'POST':
        if request.POST.get('query'):
            if request.POST.get('query')[0].isdigit():
                if request.POST.get('query').startswith('0'):
                    filtered_list = model.objects.filter(phone_number__icontains=request.POST.get('query')).values()
                    return render(request, 'data.html', context={
                        'edit':False,
                        'fields': fields,
                        'instances': filtered_list,
                        'model': page,
                        'page_name':page_name,
                        'curr_url': curr_url,
                        'form':form
                    })
                if hasattr(model, 'patient') or hasattr(model, 'psychologist'):
                    filtered_list1 = model.objects.filter(patient__id=int(request.POST.get('query'))).values()
                    filtered_list2 = model.objects.filter(psychologist__id=int(request.POST.get('query'))).values()
                    filtered_list = filtered_list1 | filtered_list2
                else:
                    filtered_list = model.objects.filter(id=int(request.POST.get('query'))).values()
                return render(request, 'data.html', context={
                    'edit':False,
                    'fields': fields,
                    'instances': filtered_list,
                    'model': page,
                    'page_name':page_name,
                    'curr_url': curr_url,
                    'form':form
                })
            else:
                if hasattr(model, 'f_name'):
                    filtered_list = model.objects.filter(f_name__icontains=request.POST.get('query')).values()
                    if hasattr(model, 'l_name'):
                        filtered_list1 = model.objects.filter(l_name__icontains=request.POST.get('query')).values()
                        filtered_list = filtered_list | filtered_list1
                    if hasattr(model, 'specialty_field'):
                        filtered_list1 = model.objects.filter(specialty_field__icontains=request.POST.get('query')).values()
                        filtered_list = filtered_list | filtered_list1
                if hasattr(model, 'name'):
                    filtered_list = model.objects.filter(name__icontains=request.POST.get('query')).values()
                if hasattr(model, 'medication_name'):
                    filtered_list = model.objects.filter(medication_name__icontains=request.POST.get('query')).values()
                
                return render(request, 'data.html', context={
                    'edit':False,
                    'fields': fields,
                    'instances': filtered_list,
                    'model': page,
                    'page_name':page_name,
                    'curr_url': curr_url,
                    'form':form
                })
        else:

            data = form(request.POST, request.FILES)
            if data.is_valid():
                data.save()
                return HttpResponseRedirect(reverse('dash', args=(curr_url,)))

    
    
    return render(request, 'data.html', context={
        'edit':False,
        'fields': fields,
        'instances': instances,
        'model': page,
        'page_name':page_name,
        'curr_url': curr_url,
        'form':form
    })


def edit(request, model, id):
    entitiy = apps.get_model('core', f'{model}')
    instance = entitiy.objects.get(id = id)
    if model == 'Psychologist':
        form = Psychologist_form
        page=f'مشاور {id}'
    elif model == 'Patient':
        form = Patient_form
        page=f'مراجع {id}'
    elif model == 'Appointment':
        form = Appointment_form
        page=f'نوبت {id}'
    elif model == 'Profit':
        form = Profit_form
        page=f'درآمد {id}'
    elif model == 'Condition':
        form = Condition_form
        page=f'تشخیص {id}'
    elif model == 'Dossier':
        form = Dossier_form
        page=f'پرونده {id}'
    elif model == 'Treatment_Plan':
        form = Treatment_Plan_form
        page=f'برنامه درمانی {id}'
    elif model == 'Medication':
        form = Medication_form
        page=f'برنامه دارویی {id}'
    else:
        form = Insurance_form
        page=f'بیمه {id}'
    if request.method =="POST":
        data = form(request.POST, request.FILES, instance=instance)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect(reverse('dash', args=(model,)))
    else:
        data = form(instance=instance)
        return render(request, 'edit.html', context={
            'edit':True,
            'page_name':page,
            'form':data,
            'model':model,
            'instance':instance
        })
    
def delete(request, model, id):
    entitiy = apps.get_model('core', f'{model}')
    instance = entitiy.objects.get(id = id)
    instance.delete()
    return HttpResponseRedirect(reverse('dash', args=(model,)))
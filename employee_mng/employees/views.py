from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def emp_home(request):

    emps = models.Emp.objects.all()
    return render(request, 'home.html', {
        'emps': emps
    })

def add_emp(request):
    if request.method == 'POST':
        # fetch data from add_emp's form ( every form has a name. we are using that)
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        # create model obj and set data
        e_obj = models.Emp()
        e_obj.name = emp_name
        e_obj.emp_id = emp_id
        e_obj.phone = emp_phone
        e_obj.address = emp_address
        # e_obj.working = emp_working
        e_obj.department = emp_department
        if emp_working is None:
            e_obj.working = False
        else:
            e_obj.working = True

        # save obj
        e_obj.save()

        return redirect('/employees/')
    return render(request, 'add_emp.html',{})


def delete_emp(request, emp_id):
    emp = models.Emp.objects.get(pk = emp_id)
    emp.delete()
    return redirect('/employees/')

def update_emp(request, emp_id):
    emp = models.Emp.objects.get(pk=emp_id)
    print('->>>>>>>>',emp_id)

    return render(request, 'update_emp.html',{
        'emp':emp
        })

def do_update_emp(request, emp_id):
    if request.method == 'POST':
        # fetch data from add_emp's form ( every form has a name. we are using that)
        emp_name = request.POST.get('emp_name')
        emp_id_temp = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        # create model obj and set data
        e_obj = models.Emp.objects.get(pk=emp_id)
        e_obj.name = emp_name
        e_obj.emp_id = emp_id_temp
        e_obj.phone = emp_phone
        e_obj.address = emp_address
        # e_obj.working = emp_working
        e_obj.department = emp_department
        if emp_working is None:
            e_obj.working = False
        else:
            e_obj.working = True

        # save obj
        e_obj.save()

    return redirect('/employees/')
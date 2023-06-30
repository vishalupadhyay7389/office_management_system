from django.shortcuts import render , HttpResponse
from .models import Department , Role , Employee
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')


def all(request):
    emps = Employee.objects.all()
    context = {
         'emps':emps
    }
    print(emps)
    return render(request,'allemp.html', context)

def addemp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept = request.POST['dept']
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name,last_name=last_name, dept_id =dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hiring_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfuly')
    elif request.method == 'GET':
        return render(request,'addemp.html')
    else:
    
        return render('An Exceptional error')


    


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employeed Removed Successfully")
        except:
            return HttpResponse("Plese Enter valid Id")
            
    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context ={
            'emps':emps
        }
        return render(request,'allemp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Exceptions Error")




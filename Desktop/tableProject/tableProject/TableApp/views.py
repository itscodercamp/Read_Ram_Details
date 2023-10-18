from django.http import HttpResponse
from django.shortcuts import render
from.models import Employee
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def HOME(request):
    data = Employee.objects.all()
    return render(request,'index.html',{'TB_Data':data})

@csrf_exempt
def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        Employee.objects.create(name = name , email = email , number = number , dob = dob , city = city , pin = pin)
        return HttpResponse('success')

@csrf_exempt
def edit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        pin = request.POST.get('pin')

        print(name)

        employee = Employee.objects.get(id=id)
        employee.name = name
        employee.email = email
        employee.number = number
        employee.dob = dob
        employee.city = city
        employee.pin = pin
        employee.save()

        return HttpResponse('success')


def edit_form(request, id):
    data = Employee.objects.get(id = id)
    return render(request,'editdata.html',{'data',data})
    

@csrf_exempt
def Delete(request):
    id = request.POST.get('id')
    emp = Employee.objects.get(id = id)
    if request.method == 'POST':
        emp.delete()
    return HttpResponse('successfully delete data')
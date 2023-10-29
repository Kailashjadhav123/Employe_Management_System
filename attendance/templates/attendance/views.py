from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Employee,Member
from .forms import Add_employee

# Create your views here.

def Home(request):
    employee_list = Employee.objects.all()
    context = {'employee_list':employee_list}
    return render(request,'attendance/home.html', context)

def add_employee(request):
    if request.method == 'POST':
        fm = Add_employee(request.POST)
        if fm.is_valid():
            fm.save()
        
    else:
        fm = Add_employee()
    return render(request, 'attendance/add_employee.html', {'fm':fm})


def Update_employee(request, id):
    if request.method=='POST':
        pi=Employee.objects.get(pk=id)
        fm=Add_employee(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Employee.objects.get(pk=id)
        fm=Add_employee(instance=pi)
    return render(request, 'attendance/update_employee.html', {'id':id, 'fm':fm})


def delete_employee(request, id):
    if request.method=="POST":
        pi = Employee.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')




def members(request):
  mymembers = Employee.objects.all().values()
  template = loader.get_template('attendance/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Employee.objects.get(id=id)
  template = loader.get_template('attendance/details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def testing(request):
    # member = Employee.objects.filter(first_name='Kavya').values()|Employee.objects.filter(id=4).values()
    template= loader.get_template('attendance/template.html')
    member = Employee.objects.filter(first_name__startswith='S')
    context= {'members':member}
    print(4+3%5)
    return HttpResponse(template.render(context, request))


def Details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

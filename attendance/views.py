from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.template import loader
from .models import Employee,Member
from .forms import Add_employee
from django.db.models import Q

# Create your views here.

def Home(request):
    employee_list = Employee.objects.all()
    # a = Employee.objects.values("pk","first_name").get(pk=1)                            # its like filter
    # a = Employee.objects.filter(Q(first_name ='Sachin') & Q(last_name = "Deshmukh"))    # Queryset with & operator
    # a = Employee.objects.filter(Q(first_name ='Sachin') | Q(last_name = "deshmukh"))    # Queryset with OR Operator
    # a = Employee.objects.filter(~Q(first_name = 'Sachin'))                              # Not Equal to
    # a = Employee.objects.filter(~Q(id=None))                                            # Filter Null object
    # a = Employee.objects.filter(id__range=(1,3))                                          # filter Between particular range
    a = Employee.objects.values('first_name','last_name')
    # for i in a:
    #   if i.contact_no:
    #     i.contact = i.contact_no + 10
    #     i.save()
    context = {'employee_list':employee_list, 'a':a}
    return render(request,'attendance/home.html', context)

def add_employee(request):
    if request.method == 'POST':
        fm = Add_employee(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = Add_employee()
    return render(request, 'attendance/add_employee.html', {'fm':fm})


def Update_employee(request, id):
    if request.method == 'POST':
        pi=Employee.objects.get(pk=id)
        fm=Add_employee(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
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
  mymembers = Member.objects.all().values()
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
    return HttpResponse(template.render(context, request))


def Details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('attendance/all_members.html')
  context = {
    'mymember': mymember}

  return HttpResponse(template.render(context, request))

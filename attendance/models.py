from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(auto_created=True, max_length=255, unique=True, )
    Address = models.CharField(max_length=255)
    contact_no = models.IntegerField()
    joining_date = models.DateField()
    leaving_date = models.DateField(blank=True, null=True)

    # def save(self,*args,**kwargs):
    #     employee_id = f"DS{self.id}"
    #     self.employee_id = employee_id
    #     save(Employee)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
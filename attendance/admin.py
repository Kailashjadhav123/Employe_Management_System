from django.contrib import admin
from .models import Employee,Member

# Register your models here.

@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'employee_id', 'Address', 'contact_no', 'joining_date','leaving_date')
    
    
    
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  
admin.site.register(Member, MemberAdmin)
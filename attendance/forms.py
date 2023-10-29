from django import forms
from .models import Employee

class Add_employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("__all__")
        
        
  
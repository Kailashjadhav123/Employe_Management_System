from django.urls import path, include
from django.contrib.auth.models import User
from attendance.models import Employee, Member
from rest_framework import routers, serializers, viewsets


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'first_name', 'last_name', 'employee_id', 'Address', 'contact_no', 
                  'joining_date', 'leaving_date']
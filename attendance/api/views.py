from django.contrib.auth.models import User
from attendance.models import Employee, Member
from rest_framework import routers, serializers, viewsets, permissions
from .serializer import EmployeeSerializer




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('leaving_date')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
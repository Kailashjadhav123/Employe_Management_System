from django.urls import path
from . import views


urlpatterns = [
    path('add_emp/', views.add_employee, name='add_employee'),
    path('update_emp/<int:id>/', views.Update_employee, name='update_employee'),
    path('delete_emp/<int:id>/', views.delete_employee, name='delete_employee'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('members/Detail/<slug:slug>/', views.Details, name='Detail'),
]

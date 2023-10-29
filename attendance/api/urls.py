from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', views.EmployeeViewSet, basename='employee' )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
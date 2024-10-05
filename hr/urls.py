from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_staff, name='register_staff'),
    path('retrieve/', views.retrieve_staff, name='retrieve_staff'),
    path('update/<str:employee_number>/', views.update_staff, name='update_staff'),
    path('api/staff/api-created/', views.retrieve_api_created_staff, name='retrieve_api_created_staff'),
]

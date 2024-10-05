from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['surname', 'other_names', 'date_of_birth', 'id_photo', 'employee_number']

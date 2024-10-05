
from django.contrib import admin
from .models import APIRequestLog
from .models import Employee
@admin.register(APIRequestLog)
class APIRequestLogAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'status_code', 'timestamp', 'ip_address', 'user')
    list_filter = ('status_code', 'method')
    search_fields = ('path', 'ip_address', 'user__username')
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'other_names', 'employee_number', 'created_via_api')
    list_filter = ('created_via_api',)  # Add a filter to easily filter API-created employees
    search_fields = ('surname', 'employee_number')  # Allows searching employees by surname and employee number


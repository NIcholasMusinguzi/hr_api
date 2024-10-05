from django.db import models
from django.contrib.auth.models import User

class APIRequestLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status_code = models.IntegerField()
    timestamp = models.DateTimeField()
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code}"


class UniqueCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Employee(models.Model):
    surname = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    id_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    employee_number = models.CharField(max_length=10, unique=True)
    created_via_api = models.BooleanField(default=False)  

    def __str__(self):
        return self.surname

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee, UniqueCode
from .serializers import EmployeeSerializer
import random

# Function to generate employee number
def generate_employee_number():
    return str(random.randint(10000, 99999))  # Customize as per your format

# Staff Registration API with unique code validation
@api_view(['POST'])
def register_staff(request):
    if request.method == 'POST':
        unique_code = request.data.get('unique_code')
        try:
            code_obj = UniqueCode.objects.get(code=unique_code, is_used=False)
        except UniqueCode.DoesNotExist:
            return Response({"detail": "Invalid or already used unique code."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()  # Make a mutable copy of the data
        data['employee_number'] = generate_employee_number()

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Mark unique code as used
            code_obj.is_used = True
            code_obj.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Staff Retrieval API
# Staff Retrieval API
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def retrieve_staff(request):
    employee_number = request.query_params.get('employee_number')

    if employee_number:
        try:
            # Retrieve a specific staff member by employee number
            employee = Employee.objects.get(employee_number=employee_number)
            serializer = EmployeeSerializer(employee)
            return Response({
                'status': 'success',
                'message': 'Employee details retrieved successfully.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({
                'status': 'error',
                'message': f'No employee found with Employee Number: {employee_number}'
            }, status=status.HTTP_404_NOT_FOUND)
    
    # If no employee number is provided, return all employees
    employees = Employee.objects.all()
    if employees.exists():
        serializer = EmployeeSerializer(employees, many=True)
        return Response({
            'status': 'success',
            'message': 'Employee list retrieved successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'status': 'error',
            'message': 'No employees found.'
        }, status=status.HTTP_404_NOT_FOUND)

# Staff Update API
@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def update_staff(request, employee_number):
    try:
        # Retrieve the staff member by employee_number
        employee = Employee.objects.get(employee_number=employee_number)
    except Employee.DoesNotExist:
        return Response({
            'status': 'error',
            'message': f'No employee found with Employee Number: {employee_number}'
        }, status=status.HTTP_404_NOT_FOUND)

    # We are only allowing updates to `date_of_birth` and `id_photo`
    allowed_fields = ['date_of_birth', 'id_photo']
    update_data = {field: request.data.get(field) for field in allowed_fields if field in request.data}

    # Ensure at least one field is provided for update
    if not update_data:
        return Response({
            'status': 'error',
            'message': 'No valid fields provided for update. Only date_of_birth and id_photo are allowed.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Update the employee with the allowed fields
    serializer = EmployeeSerializer(employee, data=update_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'Employee details updated successfully.',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response({
        'status': 'error',
        'message': 'Invalid data provided.',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
# Retrieve employees created via API
@api_view(['GET'])
def retrieve_api_created_staff(request):
    employees = Employee.objects.filter(created_via_api=True)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


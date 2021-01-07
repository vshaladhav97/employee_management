from rest_framework import serializers
from .models import Employees, Documents, AddressDetails, EmployeeStatus, DocumentVersions, EmployeeDocument, DocumentFolder, Roles



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails')

class GetEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        # fields = ('first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails')
        fields = "__all__" 
        
class AddressDetailsSerializer(serializers.ModelSerializer):
    # employees = GetEmployeesSerializer(many=True)
    employees = EmployeesSerializer(many=True)

    class Meta:
        model = AddressDetails
        fields = ("id", "address_line_1", "address_line_2", "city", "country", "pincode","employees")
        
    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        addressdetails = AddressDetails.objects.create(**validated_data)
        for employee_data in employees_data:
            Employees.objects.create(addressdetails=addressdetails, **employee_data)
        return addressdetails
    
    def update(self, instance, validated_data):
        employees_data = validated_data.pop('employees')
        employees = (instance.employees).all()
        employees = list(employees)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()

        for employee_data in employees_data:
            employee = employees.pop(0)
            employee.address_line_1 = employee_data.get('address_line_1', employee.address_line_1)
            employee.address_line_2 = employee_data.get('address_line_2', employee.address_line_2)
            employee.city = employee_data.get('city', employee.city)
            employee.country = employee_data.get('country', employee.country)
            employee.pincode = employee_data.get('pincode', employee.pincode)
            employee.save()
        return instance



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

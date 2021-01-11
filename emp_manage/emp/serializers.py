from rest_framework import serializers
from .models import Employees, Documents, AddressDetails, EmployeeStatus, DocumentVersions, EmployeeDocument, DocumentFolder, Roles

class AddressDetailsSerializer1(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails')

class GetEmployeesSerializer(serializers.ModelSerializer):
    addressdetails__address_line_1 = serializers.ReadOnlyField(source='addressdetails.address_line_1')
    addressdetails__address_line_2 = serializers.ReadOnlyField(source='addressdetails.address_line_2')
    addressdetails__city = serializers.ReadOnlyField(source='addressdetails.city')
    addressdetails__country = serializers.ReadOnlyField(source='addressdetails.country')
    addressdetails__pincode = serializers.ReadOnlyField(source='addressdetails.pincode')
    # addressdetails = serializers.ReadOnlyField(source='addressdetails')
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.context['view'].action == 'create':
    #         self.fields['addressdetails__address_line_1'].write_only = True
    #         self.fields['addressdetails__address_line_2'].write_only = True
    #         self.fields['addressdetails__city'].write_only = True
    #         self.fields['addressdetails__country'].write_only = True
    #         self.fields['addressdetails__pincode'].write_only = True
            

    class Meta:
        model = Employees
        read_only_fields = ('id', 'addressdetails__address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
        fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails', 'addressdetails__address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
    # class Meta:
    #     model = Employees
    #     fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails', 'addressdetails__address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
    #     # fields = "__all__" 

class GetEmployeesSerializer1(serializers.ModelSerializer):
    # addressdetails = AddressDetailsSerializer1()
    # addressdetails = serializers.ReadOnlyField(source='addressdetails')
    addressdetails__address_line_1 = serializers.ReadOnlyField(source='addressdetails.address_line_1')
    addressdetails__address_line_2 = serializers.ReadOnlyField(source='addressdetails.address_line_2')
    addressdetails__city = serializers.ReadOnlyField(source='addressdetails.city')
    addressdetails__country = serializers.ReadOnlyField(source='addressdetails.country')
    addressdetails__pincode = serializers.ReadOnlyField(source='addressdetails.pincode')
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.context['view'].action == 'update':
    #         self.fields['addressdetails__address_line_1'].write_only = True
    #         self.fields['addressdetails__address_line_2'].write_only = True
    #         self.fields['addressdetails__city'].write_only = True
    #         self.fields['addressdetails__country'].write_only = True
    #         self.fields['addressdetails__pincode'].write_only = True
    
    

    class Meta:
        model = Employees
        read_only_fields = ('id', 'addressdetails__address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
        fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number','addressdetails', 'addressdetails__address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
        
        def update(self, instance, validated_data):
            addressdetails = validated_data.pop('addressdetails')
            instance.addressdetails__address_line_1 = addressdetails.address_line_1
            instance.addressdetails__address_line_2 = addressdetails.address_line_2
            instance.addressdetails__city = addressdetails.city
            instance.addressdetails__country = addressdetails.country
            instance.addressdetails__pincode = addressdetails.pincode
            # ... plus any other fields you may want to update
            return instance
            
    
    # class Meta:
    #     model = Employees
    #     fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails', 'address_line_1', 'addressdetails__address_line_2', 'addressdetails__city', 'addressdetails__country', 'addressdetails__pincode')
    #     # fields = "__all__" 
        


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

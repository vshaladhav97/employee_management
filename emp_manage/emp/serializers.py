from rest_framework import serializers
from .models import Employees, AddressDetails






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

class EmployeesSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails')

class AddressDetailsSerializer1(serializers.ModelSerializer):
    # employees = GetEmployeesSerializer(many=True)
    employees_address = EmployeesSerializer1(read_only=True)

    class Meta:
        model = AddressDetails
        fields = ("id", "address_line_1", "address_line_2", "city", "country", "pincode","employees_address")
        
    def update(self, instance, validated_data):
        employees_data = validated_data.pop('employees_address')
        employees = (instance.employees_address).all()
        employees = list(employees)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.save()

        for employee_data in employees_data:
            employee = employees.pop(0)
            employee.first_name = employee_data.get('first_name', employee.first_name)
            employee.last_name = employee_data.get('last_name', employee.last_name)
            employee.username = employee_data.get('username', employee.username)
            employee.date_of_birth = employee_data.get('date_of_birth', employee.date_of_birth)
            employee.gender = employee_data.get('gender', employee.gender)
            employee.email_address = employee_data.get('email_address', employee.email_address)
            employee.contact_number = employee_data.get('contact_number', employee.contact_number)
            employee.deleted = employee_data.get('deleted', employee.deleted)
            employee.save()
        return instance

    # def update(self, instance, validated_data):
    #     employees_address = validated_data.get('employees_address')
    #     instance.employees_address.first_name = employees_address.get('first_name')
    #     instance.employees_address.last_name = employees_address.get('last_name')
    #     instance.employees_address.username = employees_address.get('username')
    #     instance.employees_address.date_of_birth = employees_address.get('date_of_birth')
    #     instance.employees_address.gender = employees_address.get('gender')
    #     instance.employees_address.email_address = employees_address.get('email_address')
    #     instance.employees_address.contact_number = employees_address.get('contact_number')
    #     instance.employees_address.deleted = employees_address.get('deleted')
    #     instance.employees_address.save()
    #     return instance
    
    
    # def update(self, instance, validated_data):
    # user_data = validated_data.pop('employees_address')
    # user_serializer = EmployeesSerializer1()
    # super(self.__class__, self).update(instance,validated_data)
    # super(EmployeesSerializer1,user_serializer).update(instance.employees_address,user_data)
    # return instance
    
    
class AddressDetailupdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddressDetails
        fields = "__all__"
            
            
    
        
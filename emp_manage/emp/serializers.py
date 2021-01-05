from rest_framework import serializers
from .models import Employees, Documents, AddressDetails, EmployeeStatus, DocumentVersions, EmployeeDocument, DocumentFolder, Roles




class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    # addressdetails = AddressDetailsSerializer()
    # roles = RoleSerializer()
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted')
        # fields = '__all__'
        
#     # def create(self, validated_data):
#     #     addressdetails = validated_data.get('addressdetails')
#     #     roles = validated_data.get('roles')
#     #     first_name = validated_data.get('first_name', None)
#     #     last_name = validated_data.get('last_name', None)
#     #     username = validated_data.get('username', None)
#     #     date_of_birth = validated_data.get('date_of_birth', None)
#     #     gender = validated_data.get('gender', None)
#     #     email_address = validated_data.get('email_address', None)
#     #     contact_number = validated_data.get('contact_number', None)
#     #     # roles = validated_data.get('roles', None)
#     #     deleted = validated_data.get('deleted', None)
#     #     employees = Employees.objects.create(first_name=first_name, last_name=last_name, gender=gender, email_address=email_address, contact_number=contact_number, addressdetails=addressdetails, roles=roles, deleted=deleted)
#     #     return employees

#     # def create(self, validated_data):
#     #     temp_bok_details = validated_data.pop('addressdetails')
#     #     temp_bok_details1 = validated_data.pop('roles')
#     #     print(validated_data)
#     #     # print()
#     #     new_book = Employees.objects.create(**validated_data)
#     #     for i in temp_bok_details:
#     #         AddressDetails.objects.create(**i,bok=new_book)
        
#     #     for i in temp_bok_details1:
#     #         Roles.objects.create(**i, bok=new_book1)
        
#     #     result = new_book + new_book1
#     #     return result
    
    
#     # # def post(self, validated_data):
#     # #     return Employees.objects.create(**validated_data)    
    
#     # def update(self, instance, validated_data):
#     #     instance.__dict__.update(**validated_data)
#     #     instance.save()
#     #     return instance

class AddressDetailsSerializer(serializers.ModelSerializer):
    # employees = EmployeesSerializer(many=True)
    class Meta:
        model = AddressDetails
        fields = ("address_line_1", "address_line_2", "city", "country", "pincode")
        # exclude = ("id", )
        
    # def create(self, validated_data):
    #     employees_data = validated_data.pop('employees')
    #     addressdetails = AddressDetails.objects.create(**validated_data)
    #     for employee_data in employees_data:
    #         Employees.objects.create(addressdetails=addressdetails, **employee_data)
    #     return addressdetails

# class AddressDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddressDetails


# class EmployeesSerializer(serializers.ModelSerializer):
#     status = serializers.SerializerMethodField()
#     class Meta:
#         model = Employees
        
# class EmpSerializer(serializers.ModelSerializer):
#     addressdetails = AddressDetailsSerializer()
#     employees = EmployeesSerializer()
#     some_field = serializers.CharField()
    


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

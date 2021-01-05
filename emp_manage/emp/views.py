from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
from rest_framework.views import APIView
from .serializers import EmployeesSerializer, DocumentSerializer, AddressDetailsSerializer, RoleSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import SignUpForm
from rest_framework.response import Response
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/show/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form': fm})


class Management(APIView):

    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeesSerializer(employee, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     # # addressdetails = get_object_or_404(AddressDetails, )
    #     serializer1 = EmployeesSerializer(data=request.data)
    #     # serializer2 = AddressDetailsSerializer(data=request.data)
    #     # serializer3 = RoleSerializer(data=request.data)
    #     # result = serializer1.data + serializer2.data + serializer3.data
    #     print(request.data)
    #     if serializer1.is_valid():
    #         serializer1.save()
    #         print(serializer1.data)
    #         return Response(serializer1.data,status=201)  # Successful post

    #     # elif serializer2.is_valid():
    #     #     serializer2.save()
    #     #     print(serializer2.data)
    #     #     return Response(serializer2.data, status=201) # Successful post

    #     # elif serializer3.is_valid():
    #     #     serializer3.save()
    #     #     print(serializer3.data)
    #     #     return Response(serializer3.data, status=201)
    #     return Response(serializer1.errors, status=400)  # Invalid data

    def post(self, request):
        json_data = request.data
        employees = {"first_name": json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
                                "date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}
        # details = {"employees": [{"first_name": json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
        #                         "date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}], "address_line_1": json_data["address_line_1"], "address_line_2": json_data["address_line_2"], "city": json_data["city"], "country": json_data["country"], "pincode": json_data["pincode"]}
        # print(details)
        
        # data = {'address_line_1': 'malabar hill', 'address_line_2': 'hanging garden', 'city': 'mumbai', 'country': 'india', 'pincode': '400006', 'employees': [{'first_name': 'vishal', 'last_name', 'pincode': '400006', 'employees': [{'first_name': 'vishal', 'last_name': 'adhav', 'username': 'vishaladhav', 'date'email_address': 'vshaladhav@gmail.com', leted': True}]}_of_birth': '1997-08-09', 'gender': 'M', 'email_address': 'vshaladhav@gmail.com', 'contact_number': 7977361393, 'deleted': True}]}
        # data = {'address_line_1': 'malabar hill', 'address_line_2': 'hanging garden', 'city': 'mumbai', 'country': 'india', 'pincode': '400006', 'employees': [{'first_name': 'vishal', 'last_name', 'pincode': '400006', 'employees': [{'first_name': 'vishal', 'last_name': 'adhav', 'username': 'vishaladhav', 'date'email_address': 'vshaladhav@gmail.com', leted': True}]}_of_birth': '1997-08-09', 'gender': 'M', 'email_address': 'vshaladhav@gmail.com', 'contact_number': 7977361393, 'deleted': True}]}
        # serializer = AddressDetailsSerializer(data=request.data)
        # employees = EmployeesSerializer(data=request.data)
        # data = {'address_line_1': 'masdlabar hill', 'address_line_2': 'hanginsdg garden', 'city': 'mumbai', 'country': 'india',
        #         'pincode': '400006', 
        #         'employees': [{'first_name': 'vsdsishal', 'last_name': 'adhav', 'username': 'vishaladhav', 'date_of_birth': '1997-08-09', 'gender': 'M', 'email_address': 'vshaladhav@gmail.com', 'contact_number': 7977361393, 'deleted': True}]}
        # emp_data = request.data
        # address_data = request.data

        # address_details = {
        #     "address_line_1": address_data["address_line_1"],
        #     "address_line_2": address_data["address_line_2"],
        #     "city": address_data["city"],
        #     "country": address_data["country"],
        #     "pincode": address_data["pincode"],
        #     "employees": address_data[
        #         {
        #             "first_name": emp_data["first_name"],
        #             "last_name": emp_data["last_name"],
        #             "username": emp_data["username"],
        #             "date_of_birth": emp_data["date_of_birth"],
        #             "gender": emp_data["gender"],
        #             "email_address": emp_data["email_address"],
        #             "contact_number": emp_data["contact_number"],
        #             "deleted": emp_data["deleted"]
        #         }
        #     ]

        # }
        # print(address_data)
        # employees = EmployeesSerializer(data=request.data)
        # request.data._mutable = True
        # request.data["employees"] = employees
        # serializer = AddressDetailsSerializer(data=data)
        # print(request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     # print(serializer.data)
        #     return Response(serializer.data, status=201)
        # return Response(serializer.errors, status=400)

        #     Employees = request.data
        #     print(Employees)

        # employees_data = request.data
        # print(employees_data)

        # roles_data = employees_data['roles']

        # emps = EmployeesSerializer(employees_data)
        # # roles = RoleSerializer(roles_data)
        # print(emps.is_valid)

        # if emps.is_valid():
        #     save_emps_data = emps.save(commit =False)
        #     save_emps_data.save()
        #     print('roles_data', roles_data)
        #     save_emps_data.roles.add(Roles.objects.get())

        # address = for(AddressDetails)

        address_data = request.data
        address_details = {
            # "id": address_data["id"],
            "address_line_1": address_data["address_line_1"],
            "address_line_2": address_data["address_line_2"],
            "city": address_data["city"],
            "country": address_data["country"],
            "pincode": address_data["pincode"]
        }
        # role_details = {
        #     "name":address_data["name"],
        #     "description":address_data["description"],
        # }
        address = AddressDetailsSerializer(data=address_details)
        # roles = RoleSerializer(data=role_details)
        print(address.is_valid())
        
        employee = EmployeesSerializer(data=employees, instance=address)
        print(employee.is_valid())
        if employee.is_valid():
            employee.save()
            return Response(employee.data, status=201)
        return Response(employee.errors, status=400)
        # print(request.data)
        # if address.is_valid() and employee.is_valid():
        #     address.save()
        #     employee.save(addressdetails = address)
            # employee.addressdetails = address
            # employee.roles = roles
            # employee.save()
        #     print(employee.data)
        #     return Response(employee.data, status=201)
        # else:
        #     print(employee.errors, address.errors, roles.errors)
        #     return Response(employee.errors, status=401)

        # serializer = EmployeesSerializer(data=request.data)

        # if serializer.is_valid():
        #     addressdetails=AddressDetails.objects.get(id=request.POST['addressdetails'])
        #     roles=Roles.objects.get(id=request.POST['roles'])
        #     serializer.save(addressdetails=addressdetails, roles=roles)
        #     return Response(serializer.data, status=200)
        # else:
        #     return Response(serializer.errors, status=400)


def clients(request):
    return render(request, "enroll/emplist.html")


def clients1(request):
    return render(request, "enroll/addemp.html")


def clients2(request):
    return render(request, "enroll/showemp.html")

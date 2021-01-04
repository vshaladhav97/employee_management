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
        
        address = AddressDetailsSerializer(data=request.data)
        # address_data = request.data
        # address = {
        #     "address_line_1": address_data["address_line_1"],
        #     "address_line_2": address_data["address_line_2"],
        #     "city": address_data["city"],
        #     "country": address_data["country"]
        #     "pincode": address_data["pincode"]
        # }
        roles = RoleSerializer(data=request.data)
        employee = EmployeesSerializer(data=request.data)
        print(request.data)
        print(address.is_valid())
        print(roles.is_valid())
        print(employee.is_valid())
        if address.is_valid() and roles.is_valid and employee.is_valid():
            address.save()
            roles.save()
            employee.save(commit=False)
            employee.addressdetails = address
            employee.roles = roles
            employee.save()
            print(employee.data)
            return Response(employee.data, status=201)
        else:
            print(employee.errors, address.errors, roles.errors)
            return Response(employee.errors, status=401)   
        
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
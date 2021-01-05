from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
from rest_framework.views import APIView
from .serializers import EmployeesSerializer, DocumentSerializer, AddressDetailsSerializer, RoleSerializer, MusicianSerializer
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

    def post(self, request):
        json_data = request.data
        details = {"employees":[{"first_name":json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
"date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}], "address_line_1":json_data["address_line_1"], "address_line_2":json_data["address_line_2"], "city":json_data["city"], "country":json_data["country"], "pincode":json_data["pincode"]}
        
        address = AddressDetailsSerializer(data=details)
        if address.is_valid():
            address.save()
            return Response(status=200)
        else:
            return Response(status=400)


def clients(request):
    return render(request, "enroll/emplist.html")


def clients1(request):
    return render(request, "enroll/addemp.html")


def clients2(request):
    return render(request, "enroll/showemp.html")


def save_data_test(self):
    details = {'address_line_1': 'masdlabar hill', 'address_line_2': 'hanginsdg garden', 'city': 'mumbai', 'country': 'india',
                'pincode': '400006', 
                'employees': [{'first_name': 'vsdsishal', 'last_name': 'adhav', 'username': 'vishaladhav', 'date_of_birth': '1997-08-09', 'gender': 'M', 'email_address': 'vshaladhav@gmail.com', 'contact_number': 7977361393, 'deleted': True}]}

    music = AddressDetailsSerializer(data=details)
    print(music.is_valid())
    if music.is_valid():
        music.save()
        return HttpResponse("success")

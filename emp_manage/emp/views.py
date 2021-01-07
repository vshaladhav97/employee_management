from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
from rest_framework.views import APIView
from .serializers import EmployeesSerializer, DocumentSerializer, AddressDetailsSerializer, RoleSerializer, GetEmployeesSerializer
from django.contrib import messages
from .forms import SignUpForm
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# signup function


@unauthenticated_user
def sign_up(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='employee')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})

# login function


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        fm = AuthenticationForm()

    return render(request, 'enroll/userlogin.html', {'form': fm})

# logout function


def logoutUser(request):
    logout(request)
    return redirect('/login/')


class Management(APIView):

    # show data
    def get(self, request):
        employee = Employees.objects.all()
        serializer = GetEmployeesSerializer(employee, many=True)
        return Response(serializer.data)

    # permissions for user and admin
    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    def post(self, request):
        json_data = request.data
        details = {"employees": [{"first_name": json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
                                "date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}], "address_line_1": json_data["address_line_1"], "address_line_2": json_data["address_line_2"], "city": json_data["city"], "country": json_data["country"], "pincode": json_data["pincode"]}

        address = AddressDetailsSerializer(data=details)
        if address.is_valid():
            address.save()
            return Response(status=200)
        else:
            return Response(status=400)


# delete and put
class ManagementDetails(APIView):

    def get_object(self, id):
        try:
            return Employees.objects.get(id=id)
        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, id):
        addressdetails = self.get_object(id)
        serializer = EmployeesSerializer(addressdetails)
        return Response(serializer.data)

    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    def put(self, request, id):
        json_data = request.data

        details = {
            "id": json_data["id"],
            "first_name": json_data["first_name"],
            "last_name": json_data["last_name"],
            "username": json_data["username"],
            "date_of_birth": json_data["date_of_birth"],
            "gender": json_data["gender"],
            "email_address": json_data["email_address"],
            "contact_number": json_data["contact_number"],
            "deleted": json_data["deleted"],
            "addressdetails": json_data[
                {
                    "id": json_data["id"],
                    "address_line_1": json_data["address_line_1"],
                    "address_line_2": json_data["address_line_2"],
                    "city": json_data["city"],
                    "country": json_data["country"],
                    "pincode": json_data["pincode"]
                }
            ]

        }

        serializer = AddressDetailsSerializer(data=details)
        print(serializer.is_valid)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    def delete(self, request, id):  # to delete record from table
        print(request.user.is_authenticated)
        addressdetails = AddressDetails.objects.get(id=id)

        addressdetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def clients(request):
    return render(request, "enroll/emplist.html")


def clients1(request):
    return render(request, "enroll/addemp.html")


def clients2(request):
    return render(request, "enroll/showemp.html")


def clients3(request):
    return render(request, "enroll/update.html")

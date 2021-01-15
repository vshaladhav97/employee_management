from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http.response import Http404, JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, AddressDetails
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from .serializers import EmployeesSerializer,  AddressDetailsSerializer,  GetEmployeesSerializer, GetEmployeesSerializer1, AddressDetailsSerializer1, AddressDetailupdateSerializer, EmployeesSerializer1
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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

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
    # print(request)
    if request.method == 'POST':

        fm = AuthenticationForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            # u = User.objects.create_user(username=uname)
            # content_type = ContentType.objects.get_for_model(BlogPost)
            # permission = Permission.objects.get(name='')
            # u.user_permissions.add(permission)
            # u.has_perm('')

            if user is not None:
                login(request, user)
                group_permissions = list(Permission.objects.filter(
                    group__user=request.user).values("codename"))
                # print(group_permissions)
                perm = []
                for group_permission in group_permissions:
                    perm.append(group_permission["codename"])
                    print(group_permission)

                # return render(request, 'enroll/showemp.html', {'perm': perm} )
                return JsonResponse({'perm': perm}, status=200)
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

        serializer1 = GetEmployeesSerializer(addressdetails)

        return Response(serializer1.data)

    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    def put(self, request, id):

        # addressdetails = AddressDetails.objects.filter(id=id).update(
        #     address_line_1, address_line_2, city, country, pincode)

        # employees = Employees.objects.filter(id=id).update(
        #     first_name="pravin", last_name="kukreja", addressdetails=addressdetails)
        # print(employees)
        # serializer = GetEmployeesSerializer1(addressdetails, data=request.data)
        # print(serializer)
        print(request.data)
        json_data = request.data
        address_data = AddressDetails.objects.get(id=id)
        address_details_data = {
            "id": json_data["id"],
            "address_line_1": json_data["address_line_1"], 
            "address_line_2": json_data["address_line_2"], 
            "city": json_data["city"], 
            "country": json_data["country"], 
            "pincode": json_data["pincode"]
        }
        addressserializer = AddressDetailupdateSerializer(data=address_details_data, instance=address_data)
        
        emp_data = Employees.objects.get(id=id)
        emp_details_data = {
            "id": json_data["id"],
            "first_name": json_data["first_name"],
            "last_name":json_data["last_name"],
            "username": json_data["username"],
            "date_of_birth":json_data["date_of_birth"],
            "gender": json_data["gender"],
            "email_address":json_data["email_address"],
            "contact_number":json_data["contact_number"],
            "addressdetails": json_data["addressdetails"],
            "deleted": json_data["deleted"]
        }
        
        empserializer = EmployeesSerializer1(data=emp_details_data, instance=emp_data)
        
        if addressserializer.is_valid() and empserializer.is_valid():
            addressserializer.save()
            empserializer.save()
            
            return Response(addressserializer.data and empserializer.data)
        return Response(addressserializer.errors and empserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    from django.views.decorators.csrf import csrf_exempt

    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    @csrf_exempt
    def delete(self, request, id):  # to delete record from table
        # print(request.user.is_authenticated)
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


def save_data_test(request, id):
    # data = {
    # "id": 60, "address_line_1": "little gibbs", "address_line_2": "malabar hill", "city": "Mumbai", "country": "india", "pincode": "400006", "employees_address": {"id": 41,"first_name": "ritin vijay","last_name": "sharma","username": "rikki","date_of_birth": "1996-01-10","gender": "M","email_address": "riki@gmail.com","contact_number": "7977361387", "addressdetails":60 ,"deleted": True}}
    if request.method == "POST":
        json_data = request.POST
        print(json_data)
        print(id)
        address = AddressDetails.objects.get(id=id)
        data = {
            "id": json_data["id"],
            "address_line_1": json_data["address_line_1"], 
            "address_line_2": json_data["address_line_2"], 
            "city": json_data["city"], 
            "country": json_data["country"], 
            "pincode": json_data["pincode"]
        }
        music = AddressDetailupdateSerializer(data=data, instance=address)
        employee = Employees.objects.get(id=json_data["id"])
        print(json_data["id"])
        print(json_data["deleted"])
        emp_data = {
            "id": json_data["id"],
            "first_name": json_data["first_name"],
            "last_name":json_data["last_name"],
            "username": json_data["username"],
            "date_of_birth":json_data["date_of_birth"],
            "gender": json_data["gender"],
            "email_address":json_data["email_address"],
            "contact_number":json_data["contact_number"],
            # "addressdetails": json_data["addressdetails"],
            "deleted": json_data["deleted"]
        }
        empserializer = EmployeesSerializer1(data=emp_data, instance=employee)
        
        print(music.is_valid())
        print(empserializer.is_valid())
        # print(empserializer.)
        if music.is_valid() and empserializer.is_valid():
            music.save()
            empserializer.save()
            # return HttpResponse("success")
            return JsonResponse({"success":"success"} ,status=status.HTTP_201_CREATED)
        return JsonResponse({"error":"error"},status=status.HTTP_400_BAD_REQUEST)

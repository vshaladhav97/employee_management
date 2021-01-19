from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http.response import Http404, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, AddressDetails
from rest_framework.views import APIView

from .serializers import AddressDetailsSerializer,  GetEmployeesSerializer, AddressDetailupdateSerializer, EmployeesSerializer1
from django.contrib import messages
from .forms import SignUpForm
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Permission

# Create your views here.

# signup function


@unauthenticated_user
def sign_up(request):
    """This function is used to perform sign up of user and assign group to the user."""
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
    """This function is used to perform login of existing user."""
    if request.method == 'POST':

        fm = AuthenticationForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                group_permissions = list(Permission.objects.filter(
                    group__user=request.user).values("codename"))

                perm = []
                for group_permission in group_permissions:
                    perm.append(group_permission["codename"])
                    

                return JsonResponse({'perm': perm}, status=200)
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        fm = AuthenticationForm()

    return render(request, 'enroll/userlogin.html', {'form': fm})

# logout function


def logoutUser(request):
    """This logoutUser() function is used to perform logout of existing user."""
    logout(request)
    return redirect('/login/')


class Management(APIView):
    """This class is used to manage user data."""
    

    def get(self, request):
        """Get tha Employees data."""
        employee = Employees.objects.all()
        serializer = GetEmployeesSerializer(employee, many=True)
        return Response(serializer.data)

    # permissions for user and admin.
    @method_decorator(login_required(login_url='login'), name='dispatch')
    @method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
    # for posting data to data base.
    def post(self, request):
        """Post the Employees data."""
        json_data = request.data
        details = {"employees": [{"first_name": json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
                                  "date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}], "address_line_1": json_data["address_line_1"], "address_line_2": json_data["address_line_2"], "city": json_data["city"], "country": json_data["country"], "pincode": json_data["pincode"]}

        address = AddressDetailsSerializer(data=details)
        if address.is_valid():
            address.save()
            return Response(status=200)
        else:
            return Response(status=400)


class ManagementDetails(APIView):
    """This class is used to perform getting data and delete row in database through rest framework."""

    def get_object(self, id):
        """Get the Employees data with Id"""
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
        """update the Employees Data by Employees Id."""
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
        addressserializer = AddressDetailupdateSerializer(
            data=address_details_data, instance=address_data)

        emp_data = Employees.objects.get(id=id)
        emp_details_data = {
            "id": json_data["id"],
            "first_name": json_data["first_name"],
            "last_name": json_data["last_name"],
            "username": json_data["username"],
            "date_of_birth": json_data["date_of_birth"],
            "gender": json_data["gender"],
            "email_address": json_data["email_address"],
            "contact_number": json_data["contact_number"],
            "addressdetails": json_data["addressdetails"],
            "deleted": json_data["deleted"]
        }

        empserializer = EmployeesSerializer1(
            data=emp_details_data, instance=emp_data)

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
        """This Function is used to delete Employees."""
        addressdetails = AddressDetails.objects.get(id=id)
        addressdetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def clients1(request):
    """This function is used to redirect to template to add employees."""
    current_user = request.user
    user_name = current_user.username

    context = {'user_name': user_name}
    return render(request, "enroll/addemp.html", context)


def clients2(request):
    """This function is used to redirect to template to show employees."""
    current_user = request.user
    user_name = current_user.username

    context = {'user_name': user_name}
    return render(request, "enroll/showemp.html", context)


def clients3(request):
    return render(request, "enroll/update.html")


def save_data_test(request, id):
    """This is used to perform updating row in database through rest framework."""
    if request.method == "POST":
        json_data = request.POST

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

        emp_data = {
            "id": json_data["id"],
            "first_name": json_data["first_name"],
            "last_name": json_data["last_name"],
            "username": json_data["username"],
            "date_of_birth": json_data["date_of_birth"],
            "gender": json_data["gender"],
            "email_address": json_data["email_address"],
            "contact_number": json_data["contact_number"],

            "deleted": json_data["deleted"]
        }
        empserializer = EmployeesSerializer1(data=emp_data, instance=employee)

        if music.is_valid() and empserializer.is_valid():
            music.save()
            empserializer.save()

            return JsonResponse({"success": "success"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)

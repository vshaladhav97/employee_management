from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import EmployeeForm, DocumentsForm, EmployeeStatusForm, AddressDetailsForm, RolesForm, DocumentVersionsForms, EmployeeDocumentForm, DocumentFolderForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .decorators import unauthenticated_user
# Create your views here.
# @unauthenticated_user
# def registerPage(request):

#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')

#             group = Group.objects.get(name='staffs')
#             user.groups.add(group)

#             messages.success(request, 'Account was created for ' + username)

#             return redirect('login')

#     context = {'form': form}
#     return render(request, 'enroll/register.html', context)

# @unauthenticated_user
# def loginPage(request):

# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password =request.POST.get('password')

# 		user = authenticate(request, username=username, password=password)

# 		if user is not None:
# 			login(request, user)
# 			return redirect('/show')
# 		else:
# 			messages.info(request, 'Username OR password is incorrect')

# 	context = {}
# 	return render(request, 'enroll/login.html', context)

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

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


def user_profile(request):
    return render(request, 'enroll/profile.html')


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:

                form.save()
                return redirect('/show')
            except:
                return "invalid data"
    else:
        form = EmployeeForm()
    return render(request, 'enroll/index.html', {'form': form})


def show(request):
    employees = Employees.objects.all()
    return render(request, "enroll/show.html", {"employees": employees})


def edit(request, id):
    if request.method == 'POST':
        pi = Employees.objects.get(id=id)
        form = EmployeeForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        pi = Employees.objects.get(id=id)
        form = EmployeeForm(request.POST, instance=pi)
    return render(request, "enroll/edit.html", {'form': form})

# def update(request, id):
#     employees = Employees.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=employees)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, "enroll/edit.html", {'employees': employees})


def delete(request, id):
    employees = Employees.objects.get(id=id)
    employees.delete()
    return redirect("/show")


def emp1(request):
    if request.method == 'POST':
        form = EmployeeStatusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return "invalid data"
    else:
        form = EmployeeStatusForm()
    return render(request, 'enroll/index1.html', {'form': form})

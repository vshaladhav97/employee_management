from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
from django import forms


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EmployeeStatusForm(forms.ModelForm):
    class Meta:
        model = EmployeeStatus
        fields = "__all__"


class AddressDetailsForm(forms.ModelForm):
    class Meta:
        model = AddressDetails
        fields = "__all__"


class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = "__all__"


class DocumentVersionsForms(forms.ModelForm):
    class Meta:
        model = DocumentVersions
        fields = "__all__"


class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDocument
        fields = "__all__"


class DocumentFolderForm(forms.ModelForm):
    class Meta:
        model = DocumentFolder
        fields = "__all__"

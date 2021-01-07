from django.contrib import admin
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
# Register your models here.
admin.site.register(Employees)
admin.site.register(Documents)
admin.site.register(AddressDetails)
admin.site.register(EmployeeStatus)
admin.site.register(Roles)
admin.site.register(DocumentVersions)
admin.site.register(EmployeeDocument)
admin.site.register(DocumentFolder)

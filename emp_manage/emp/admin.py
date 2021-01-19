from django.contrib import admin
from .models import Employees, AddressDetails
# Register your models here.
admin.site.register(Employees)
# @admin.register(Employees)
# class EmployeesAdmin(admin.ModelAdmin):
#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     # to disable view and add you can do this 
#     def has_view_permission(self, request, obj=None):
#         return True

#     def has_add_permission(self, request):
#         return False
# admin.site.register(Documents)
admin.site.register(AddressDetails)
# admin.site.register(EmployeeStatus)
# admin.site.register(Roles)
# admin.site.register(DocumentVersions)
# admin.site.register(EmployeeDocument)
# admin.site.register(DocumentFolder)

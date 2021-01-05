from django.db import models

# Create your models here.
class EmployeeStatus(models.Model):
    # id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.status)


class AddressDetails(models.Model):
    # id = models.AutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=8)
    
    def __str__(self):
        return self.country


class Roles(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name, self.description


class Employees(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_address = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=20)
    addressdetails = models.ForeignKey(AddressDetails, on_delete=models.CASCADE, related_name="addressdetails", null=True)
    # roles = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="roles", null=True)
    deleted = models.BooleanField()
    
    def __str__(self):
        return self.first_name


class Documents(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    guid = models.CharField(max_length=36)
    description = models.CharField(max_length=255)


class DocumentVersions(models.Model):
    documents = models.ForeignKey(Documents, on_delete=models.CASCADE)
    guid = models.CharField(max_length=50)
    version = models.SmallIntegerField(6)
    uploaded_time = models.DateTimeField()
    extension = models.CharField(max_length=9)
    content_type = models.CharField(max_length=75)
    size = models.IntegerField()
    uploaded_by = models.ForeignKey(Employees, on_delete=models.CASCADE)


class EmployeeDocument(models.Model):
    # id = models.AutoField(primary_key=True)
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    documentversion = models.ForeignKey(DocumentVersions, on_delete=models.CASCADE)


class DocumentFolder(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)
    documentversions = models.ForeignKey(DocumentVersions, on_delete=models.CASCADE)
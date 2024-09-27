from django.db import models

# admin.site.register(Employees)
# Create your models here.

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

class Students(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=255)
    Studentaddress = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
     
def __str__(self):
    return self


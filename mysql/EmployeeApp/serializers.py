from rest_framework import serializers 
from EmployeeApp.models import Department,Employees,Students

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentId','DepartmentName')


 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('StudentId','StudentName','Studentaddress','City')
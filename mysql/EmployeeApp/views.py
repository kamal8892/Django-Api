from django.shortcuts import render
from .models import Employees
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employees,Students
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer,StudentSerializer

 
# Create your views here.


@csrf_exempt
def departmentApi(request,id=None):
    if request.method=='GET':
        department = Department.objects.all()
        department_serializer=DepartmentSerializer(department,many=True)
        return JsonResponse(department_serializer.data,safe=False)
        
    
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Updated")
    
    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Updated")
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        students = Students.objects.all()
        Students_serializer=StudentSerializer(students,many=True)
        return JsonResponse(Students_serializer.data,safe=False)
    
    elif request.method=='POST':
        students_data = JSONParser().parse(request)
        Students_serializer=StudentSerializer(data=students_data)
        if Students_serializer.is_valid():
            Students_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        students_data=JSONParser().parse(request)
        students=Students.objects.get(StudentId=students_data['StudentId'])
        Students_serializer=StudentSerializer(students,data=students_data)
        if Students_serializer.is_valid():
            Students_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Updated")
    
    elif request.method=='DELETE':
        students=Students.objects.get(StudentId=id)
        students.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


     
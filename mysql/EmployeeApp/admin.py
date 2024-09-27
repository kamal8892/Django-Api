# from django.contrib import admin
# from .models import Employees,Department,Students

# admin.site.register(Employees,Department,Students)

# # Register your models here.
from django.contrib import admin
from .models import Employees, Department, Students

admin.site.register(Employees)
admin.site.register(Department)
admin.site.register(Students)

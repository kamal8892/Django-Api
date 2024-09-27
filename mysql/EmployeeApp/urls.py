from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
]

urlpatterns = [
    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),
]

urlpatterns = [
    re_path(r'^students$', views.studentApi),
    re_path(r'^students/([0-9]+)$', views.studentApi),
]
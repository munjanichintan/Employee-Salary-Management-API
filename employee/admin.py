from django.contrib import admin
from .models import Employee, Salary

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'ename', 'eemail', 'econtact')

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'eid', 'esalary')

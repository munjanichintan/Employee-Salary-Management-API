from django.db import models

# Create your models here.
class Employee(models.Model):
	eid = models.IntegerField(primary_key=True)
	ename = models.CharField(max_length=100)
	eemail = models.EmailField()
	econtact = models.CharField(max_length=10)
	class Meta:
		db_table = "employee"

	def __str__(self):
		return self.ename

class Salary(models.Model):
	id = models.IntegerField(primary_key=True)
	eid = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
	esalary = models.IntegerField()

	class Meta:
		db_table = "salary"
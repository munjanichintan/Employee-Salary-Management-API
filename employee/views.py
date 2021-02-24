from django.shortcuts import render, redirect
from employee.forms import EmployeeForm,  SalaryForm
from employee.models import Employee, Salary


def emp(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request, 'index.html', {'form':form})

# def indexsal(request):

# 	employees = Employee.objects.all()
# 	return render(request, 'indexsal.html', {'employees':employees})

def indexsal1(request):
	if request.method == 'POST':
		# nid = request.POST.get("nid")
		esalary = request.POST.get("esalary")
		salary_id = request.POST.get("empid")
		eid = Employee.objects.get(eid=salary_id)
		Salary.objects.create(esalary=esalary, id=salary_id, eid=eid)
		return redirect('/showsal')

	else:
		return render(request, 'indexsal.html', {'employees': Employee.objects.all()})


def show(request):
	employees = Employee.objects.all()
	return render(request, 'show.html', {'employees':employees})

def showsal(request):
	employees = Salary.objects.all()
	return render(request, 'showsal.html', {'employees':employees})


def edit(request, id):
	employee = Employee.objects.get(eid=id)
	return render(request, 'edit.html', {'employee':employee})

def editsal(request, id):
	employee = Salary.objects.get(id=id)
	return render(request, 'editsal.html', {'employee':employee})

def update(request, id):
	employee = Employee.objects.get(eid=id)
	form = EmployeeForm(request.POST, instance = employee)
	if form.is_valid():
		form.save()
		return redirect('/show')
	return render(request, 'edit.html', {'employee':employee})

def updatesal(request, id):
	employee = Salary.objects.get(id=id)
	form = SalaryForm(request.POST, instance = employee)
	print(request.POST, "post")
	if form.is_valid():
		form.save()
		return redirect('/showsal')
	return render(request, 'editsal.html', {'employee':employee})

def destroy(request, id):
	employee = Employee.objects.get(eid=id)
	employee.delete()
	return redirect('/show')

def salary(request):
	employees = Employee.objects.all()
	return render(request, 'salary.html', {'employees': employees, 'salary': salary})

def destroysal(request, id):
	employee = Salary.objects.get(eid=id)
	employee.delete()
	return redirect('/showsal')
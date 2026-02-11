from django.shortcuts import render, redirect
from .models import Employee
from django.contrib import messages


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees/employee_list.html", {"employees": employees})


def employee_create(request):
    # Handle form submission
    if request.method == "POST":
        # Get form data (NO employee_id here)
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        department = request.POST.get("department")

        # Validation: all fields required
        if not all([full_name, email, department]):
            messages.error(request, "All fields are required")
            return redirect("employee_create")

        # Validation: email must be unique
        if Employee.objects.filter(email=email).exists():
            messages.error(request, "An employee with this email already exists")
            return redirect("employee_create")

        # Create employee
        # employee_id will be auto-generated in model.save()
        Employee.objects.create(full_name=full_name, email=email, department=department)

        # Success message
        messages.success(request, "Employee added successfully")
        return redirect("employee_list")

    # GET request → show form
    return render(request, "employees/employee_form.html")


def employee_delete(request, pk):
    Employee.objects.filter(id=pk).delete()
    return redirect("employee_list")

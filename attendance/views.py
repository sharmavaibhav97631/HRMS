from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Attendance
from employees.models import Employee


def mark_attendance(request):
    employees = Employee.objects.all()

    if request.method == "POST":
        employee_id = request.POST.get("employee")
        date = request.POST.get("date")
        status = request.POST.get("status")

        if not all([employee_id, date, status]):
            messages.error(request, "All fields are required")
            return redirect("mark_attendance")

        employee = Employee.objects.get(id=employee_id)

        if Attendance.objects.filter(employee=employee, date=date).exists():
            messages.error(request, "Attendance already marked for this date")
            return redirect("mark_attendance")

        Attendance.objects.create(employee=employee, date=date, status=status)

        messages.success(request, "Attendance marked successfully")
        return redirect("attendance_list")

    return render(request, "attendance/attendance_list.html", {"employees": employees})


def attendance_list(request):
    records = Attendance.objects.select_related("employee")
    employees = Employee.objects.all()

    employee_id = request.GET.get("employee")

    if employee_id:
        records = records.filter(employee__id=employee_id)

    return render(
        request,
        "attendance/attendance_list.html",
        {"records": records, "employees": employees},
    )

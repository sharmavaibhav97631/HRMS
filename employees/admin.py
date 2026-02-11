from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = (
        "employee_id",
        "full_name",
        "email",
        "department",
    )

    # Make employee_id read-only (cannot be edited)
    readonly_fields = ("employee_id",)

    # Enable search in admin
    search_fields = (
        "employee_id",
        "full_name",
        "email",
        "department",
    )

    # Filters on right sidebar
    list_filter = ("department",)

    # Default ordering
    ordering = ("employee_id",)

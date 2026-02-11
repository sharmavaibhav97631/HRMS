from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and not self.employee_id:
            self.employee_id = f"EMP{self.id:04d}"
            super().save(update_fields=["employee_id"])

    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.db.models.fields import (
    DateField,
    FloatField
)
from salary.managers import SalaryManager
from users.models import User


class Salary(models.Model):
    salary = FloatField()
    discounts = FloatField()
    date = DateField()
    user = ForeignKey(User, on_delete=CASCADE, related_name='salaries')
    objects = SalaryManager()

from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields import (
    CharField,
    DateField
)
from cpf_field.models import CPFField
from users.managers import UserManager


class User(models.Model):
    cpf = CPFField('cpf', unique=True)
    name = CharField(max_length=155, verbose_name='Name')
    born_date = DateField()
    objects = UserManager()

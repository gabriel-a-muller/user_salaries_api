from typing import Any
from typing import TypeVar as _T
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(models.Manager):
    def create(self, **obj_data: Any) -> _T:
        if not isinstance(obj_data['cpf'], str):
            raise ValidationError
        obj_data['cpf'] = obj_data['cpf'].replace('.', '').replace('-', '')
        return super().create(**obj_data)

    def update(self, **obj_data: Any) -> int:
        if not isinstance(obj_data['cpf'], str):
            raise ValidationError
        obj_data['cpf'] = obj_data['cpf'].replace('.', '').replace('-', '')
        return super().update(**obj_data)

from typing import Any
from typing import TypeVar as _T
from django.db import models


class SalaryManager(models.Manager):
    def create(self, **obj_data: Any) -> _T:
        return super().create(**obj_data)

    def update(self, **obj_data: Any) -> int:
        return super().update(**obj_data)

    def _get_average(self, field: str) -> dict:
        result_list = self.model.objects.values_list(field, flat=True)
        total_count = len(result_list)
        average = sum(result_list) / total_count
        response_dict = {
            'total_count': total_count,
            'average': average
        }
        return response_dict

    def get_salary_average(self) -> dict:
        return self._get_average('salary')

    def get_discounts_average(self) -> dict:
        return self._get_average('discounts')

    def get_min_salary(self) -> object:
        min_salary = self.model.objects.all().order_by('salary').first()
        return min_salary

    def get_max_salary(self) -> object:
        max_salary = self.model.objects.all().order_by('salary').last()
        return max_salary

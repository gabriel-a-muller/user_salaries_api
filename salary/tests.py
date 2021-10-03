import datetime
from django.core.exceptions import ValidationError
from django.test import TestCase
from salary.models import Salary
from users.models import User


class SalaryTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            cpf='352.083.230-52',
            name='User1',
            born_date=datetime.date.today())
        
        self.user2 = User.objects.create(
            cpf='64477087039',
            name='User2',
            born_date=datetime.date.today())

        self.user3 = User.objects.create(
            cpf='91895876001',
            name='User3',
            born_date=datetime.date.today())

    def test_create_salary(self):
        salary1 = Salary.objects.create(
            salary=1000.57,
            discounts=500.57,
            date=datetime.date.today(),
            user=self.user1
        )
        salary2 = Salary.objects.create(
            salary=2000.57,
            discounts=500.57,
            date=datetime.date.today(),
            user=self.user1
        )
        self.assertTrue(Salary.objects.filter(id=salary1.id).exists())
        self.assertTrue(Salary.objects.filter(id=salary2.id).exists())
        Salary.objects.filter(id=salary1.id).delete()
        Salary.objects.filter(id=salary2.id).delete()
        self.assertFalse(Salary.objects.filter(id=salary1.id).exists())
        self.assertFalse(Salary.objects.filter(id=salary2.id).exists())

    def test_edit_salary(self):
        salary = Salary.objects.create(
            salary=1000.57,
            discounts=500.57,
            date=datetime.date.today(),
            user=self.user1
        )
        self.assertTrue(Salary.objects.filter(id=salary.id).exists())
        Salary.objects.filter(id=salary.id).update(salary=7777)
        salary = Salary.objects.get(id=salary.id)
        self.assertTrue(salary.salary == 7777)
        self.assertTrue(Salary.objects.filter(id=salary.id).exists())
        Salary.objects.filter(id=salary.id).delete()
        self.assertFalse(Salary.objects.filter(id=salary.id).exists())

    def test_check_averages(self):
        salary1 = Salary.objects.create(
            salary=1000.57,
            discounts=500.77,
            date=datetime.date.today(),
            user=self.user1
        )
        salary2 = Salary.objects.create(
            salary=2000.57,
            discounts=600.77,
            date=datetime.date.today(),
            user=self.user2
        )
        salary3 = Salary.objects.create(
            salary=3000.57,
            discounts=700.77,
            date=datetime.date.today(),
            user=self.user3
        )
        salary_average = Salary.objects.get_salary_average()
        discounts_average = Salary.objects.get_discounts_average()
        self.assertTrue(salary_average['total_count'] == 3)
        self.assertTrue(discounts_average['total_count'] == 3)
        self.assertTrue(salary_average['average'] == 2000.57)
        self.assertTrue(discounts_average['average'] == 600.77)
        self.assertTrue(Salary.objects.get_min_salary().salary == 1000.57)
        self.assertTrue(Salary.objects.get_max_salary().salary == 3000.57)
        Salary.objects.filter(id=salary1.id).delete()
        Salary.objects.filter(id=salary2.id).delete()
        Salary.objects.filter(id=salary3.id).delete()

    def test_cascade_user(self):
        salary1 = Salary.objects.create(
            salary=1000.57,
            discounts=500.77,
            date=datetime.date.today(),
            user=self.user1
        )
        salary2 = Salary.objects.create(
            salary=1000.57,
            discounts=500.77,
            date=datetime.date.today(),
            user=self.user1
        )
        self.assertTrue(User.objects.filter(id=self.user1.id).exists())
        self.assertTrue(Salary.objects.filter(id=salary1.id).exists())
        self.assertTrue(Salary.objects.filter(id=salary2.id).exists())
        User.objects.filter(id=self.user1.id).delete()
        self.assertFalse(User.objects.filter(id=self.user1.id).exists())
        self.assertFalse(Salary.objects.filter(id=salary1.id).exists())
        self.assertFalse(Salary.objects.filter(id=salary2.id).exists())

    def test_check_discount_value(self):
        self.assertRaises(ValidationError, Salary.objects.create, 
            salary=10,
            discounts=20,
            date=datetime.date.today(),
            user=self.user1)

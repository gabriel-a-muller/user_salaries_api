import datetime
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from django.db import transaction
from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        pass

    def test_cpf_create_user(self):
        test_date = datetime.date.today()
        user = User.objects.create(
            cpf='352.083.230-52',
            name='Gabriel',
            born_date=test_date)
        self.assertTrue(User.objects.filter(id=user.id).exists())
        User.objects.filter(id=user.id).delete()
        self.assertFalse(User.objects.filter(id=user.id).exists())

        user = User.objects.create(
            cpf='64477087039',
            name='Gabriel',
            born_date=test_date)
        self.assertTrue(User.objects.filter(id=user.id).exists())
        User.objects.filter(id=user.id).delete()
        self.assertFalse(User.objects.filter(id=user.id).exists())

        try:
            with transaction.atomic():
                user = User(cpf='123', name='Test', born_date=test_date)
                user.full_clean()
            self.fail("Invalid CPF")
        except ValidationError:
            pass

        try:
            with transaction.atomic():
                user = User.objects.create(
                    cpf='11111111111', name='UserTest', born_date=test_date)
                user.full_clean()
            self.fail("Invalid CPF")
        except ValidationError:
            pass

    def test_date_create_user(self):
        cpf = '64477087039'
        name = 'UserTest'
        ok_date = datetime.date.today()

        try:
            with transaction.atomic():
                user = User.objects.create(
                    cpf=cpf, name=name, born_date='2020/12/12')
            self.fail("Invalid Date")
        except ValidationError:
            pass

        try:
            with transaction.atomic():
                user = User.objects.create(
                    cpf=cpf, name=name, born_date='testing')
            self.fail("Invalid Date")
        except ValidationError:
            pass

        user = User.objects.create(
            cpf=cpf,
            name=name,
            born_date=ok_date)
        self.assertTrue(User.objects.filter(id=user.id).exists())
        User.objects.filter(id=user.id).delete()
        self.assertFalse(User.objects.filter(id=user.id).exists())

    def test_edit_user(self):
        cpf = '64477087039'
        name = 'UserTest'
        ok_date = datetime.date.today()

        user = User.objects.create(
            cpf=cpf,
            name=name,
            born_date=ok_date)
        self.assertTrue(User.objects.filter(id=user.id).exists())

        User.objects.filter(id=user.id).update(name='ChangedName')
        user = User.objects.get(name='ChangedName')
        self.assertTrue(user.name == 'ChangedName')
        self.assertTrue(User.objects.filter(id=user.id).exists())

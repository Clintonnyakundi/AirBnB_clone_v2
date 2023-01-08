#!/usr/bin/python3
""" module to test User"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """ unittest class"""

    def __init__(self, *args, **kwargs):
        """ initialize tests"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test property: first_name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test property: last_name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test attribute: email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test attribute: password"""
        new = self.value()
        self.assertEqual(type(new.password), str)

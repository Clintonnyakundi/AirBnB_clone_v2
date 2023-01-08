#!/usr/bin/python3
""" module"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """ unittest class"""

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test attribute: name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

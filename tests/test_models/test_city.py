#!/usr/bin/python3
"""module for the unittest of the City model """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """The unittest cases for the City """

    def __init__(self, *args, **kwargs):
        """initialize the tests """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing the State.id of the City """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test the name of the City"""
        new = self.value()
        self.assertEqual(type(new.name), str)

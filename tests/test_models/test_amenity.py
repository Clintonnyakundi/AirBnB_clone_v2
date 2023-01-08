#!/usr/bin/python3
"""write tests for Amenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """unittests for Amenity class """

    def __init__(self, *args, **kwargs):
        """Instantiate Amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name of Amenity instance"""
        new = self.value()
        self.assertEqual(type(new.name), str)

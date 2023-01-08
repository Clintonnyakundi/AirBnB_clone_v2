#!/usr/bin/python3
""" module"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """unittest class """

    def __init__(self, *args, **kwargs):
        """ initialize tests"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test attribute: place_id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test attribute: user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test attribute: text"""
        new = self.value()
        self.assertEqual(type(new.text), str)

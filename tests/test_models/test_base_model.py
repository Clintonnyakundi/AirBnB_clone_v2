#!/usr/bin/python3
""" module for the test cases for the BaseModel """
import unittest
from models.base_model import BaseModel
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """ unittest cases for the BaseModel model """

    def __init__(self, *args, **kwargs):
        """initialize a BaseModel instance """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up the unittest """
        pass

    def tearDown(self):
        """clean up after the tests"""
        try:
            os.remove('file.json')
        except Exception as msg:
            pass

    def test_default(self):
        """ first test case: test that the types actually match"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test case: kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test case kwargs_int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Test case: the string repr. of an instance"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.__dict__))

    def test_todict(self):
        """test to dict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test no kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    # def test_kwargs_one(self):
    #     """ test one keyword argument """
    #     with self.assertRaises(KeyError):
    #         new = self.value(**{"Arbitrary": "test"})

    def test_id(self):
        """ test case for the id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test the `created_at` property """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test the `updated_at` property"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new1 = BaseModel(**n)
        self.assertFalse(new1.created_at == new1.updated_at)

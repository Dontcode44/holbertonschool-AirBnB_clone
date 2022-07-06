#!/usr/bin/python3
from datetime import datetime
import unittest
from models import storage
from models.base_model import BaseModel
"""unitest for basemodel.py class BaseModel"""


class tests_BaseModel(unittest.TestCase):
    """Tests for FileStorage class"""
    my_model = BaseModel()

    def testing(self):
        """testing - Test dict"""
        self.assertIsNotNone(self.my_model)
        self.assertIsInstance(storage.all(), dict)
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.id, str)

    def test_exist_class(self):
        """Test if the class exist"""
        self.assertEqual(str(type(self.my_model)),
        "<class 'models.base_model.BaseModel'>")

if __name__ == '__main__':
    unittest.main()

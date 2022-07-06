#!/usr/bin/python3
"""unitest for basemodel.py class BaseModel"""


from datetime import datetime
import unittest
from models import storage
from models.base_model import BaseModel


class Tests_BaseModel(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()

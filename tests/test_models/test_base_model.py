#!/usr/bin/python3
"""unitest for basemodel.py class BaseModel"""


from datetime import datetime
import unittest
from models import storage
from models.base_model import BaseModel


class Tests_BaseModel(unittest.TestCase):
    """Tests for FileStorage class"""

    def testing(self):
        """testing - Test dict"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """Atributes of the class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

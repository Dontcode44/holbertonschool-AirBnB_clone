#!/usr/bin/python3
"""Review class from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Atributes of the class"""
    place_id = ""
    user_id = ""
    text = ""

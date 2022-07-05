#!/usr/bin/python3
"""FileStorage - create a unique FileStorage
instance for your application"""

from imp import reload
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

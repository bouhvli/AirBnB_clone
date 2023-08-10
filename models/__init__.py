#!/usr/bin/python3
"""
The module creates a unique FileStorage instance
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
#!/usr/bin/python3
"""The module initalizes the models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


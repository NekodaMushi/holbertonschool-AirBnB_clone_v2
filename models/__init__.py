
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
"""for using getenv to determine with which kind of storage we work"""

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

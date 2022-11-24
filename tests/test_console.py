#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from unittest.mock import patch
import pycodestyle
import console
from console import HBNBCommand
from io import StringIO
import cmd
import json
import models
import unittest
import os
from itertools import count

def	test_pycodstyle(self):
	"""Checks if the syntax is right (pip8)"""
	syntax = pycodestyle.Styleguide(quiet=True)
	result = syntax.check_files(["console.py"])
	self.assertEqual(
		result.total_errors, 0, "Errors pycodestyle."
	)

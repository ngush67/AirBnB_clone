#!/usr/bin/env python3
'''Packages a bunch of modules'''

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

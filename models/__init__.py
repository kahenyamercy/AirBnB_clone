#!/usr/bin/python3
from .engine.file_storage import FileStorage

# Restore all the saved objects
storage = FileStorage()
storage.reload()

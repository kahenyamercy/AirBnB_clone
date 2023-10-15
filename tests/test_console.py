#!/usr/bin/python3
"""Test for console"""

import sys
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):
    '''Test the console module'''

    def setUp(self):
        '''Setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        '''Teardown'''
        sys.stdout = self.backup

    def create(self):
        '''Create an instance of the HBNBCommand class'''
        return HBNBCommand()

    def test_quit(self):
        '''Test quit exists'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        '''Test EOF exists'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        '''Test all exists'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name_doesnt_exist(self):
        '''Test error messages for class name missing.'''
        console = self.create()
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("create Binita")
        x = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.assertEqual("** class doesn't exist **\n", x)

    def test_create(self):
        '''Test that create works for BaseModel.'''
        console = self.create()
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("create BaseModel")
        x = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.assertTrue(len(x) > 0)

    def test_show(self):
        '''Test that show works for BaseModel.'''
        console = self.create()
        console.onecmd("create BaseModel")
        obj_id = self.capt_out.getvalue().strip()
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"show BaseModel {obj_id}")
        x = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    
    def test_update(self):
        '''test_update method'''
        console = self.create()  # Instantiate HBNBCommand using the create method
        console.onecmd("create BaseModel")
        obj_id = self.capt_out.getvalue().strip()
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"update BaseModel {obj_id} name 'New Name'")
        console.onecmd(f"show BaseModel {obj_id}")
        output = self.capt_out.getvalue().strip()
        print(output)

    def test_destroy(self):
        '''Test that destroy works for BaseModel.'''
        console = self.create()
        console.onecmd("create BaseModel")
        obj_id = self.capt_out.getvalue().strip()
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd(f"destroy BaseModel {obj_id}")
        console.onecmd(f"show BaseModel {obj_id}")
        x = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n".strip(), x.strip())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter for the AirBnB_clone
    """
    prompt = '(hbnb) '
    class_name_to_class = {
            "BaseModel": BaseModel
            }

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True


    def do_EOF(self, line):
        """
        Handle end of file
        """
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of class,
        saves it (to the JSON file) and prints the id

        Returns:
            On successful instantiation, it returns
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = self.search_for_class(args[0])
        if not class_name:
            return
        class_instance = self.class_name_to_class[class_name]()
        class_instance.save()
        print(class_instance.id)

    def search_for_class(self, name):
        for key, value in self.class_name_to_class.items():
            if name == key:
                return key
            print("** class doesn't exist **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

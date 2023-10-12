#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = self.search_for_class(args[0]);
        if class_name:
            name_and_id = f"{args[0]}.{args[1]}"
            objects = storage.all()
            for key, value in objects.items():
                if key == name_and_id:
                    print(objects[key])
                    new_instance = self.class_name_to_class[class_name](**objects[key])
                    print(new_instance)

    def search_for_class(self, name):
        for key, value in self.class_name_to_class.items():
            if name == key:
                return key
            print("** class doesn't exist **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

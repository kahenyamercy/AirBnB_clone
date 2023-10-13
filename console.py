#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter for the AirBnB_clone
    """
    prompt = '(hbnb) '
    class_name_to_class = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Review": Review,
            "Amenity": Amenity
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

    def default(self, line):
        """
        Handles other cases where users use valid syntax
        which may not be necessarily commands
        """
        name, method = line.split('.')
        if method == 'all()':
            self.do_all(name)

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
        class_name = self.search_for_class(args[0]);
        if class_name:
            if len(args) < 2:
                print("** instance id missing **")
                return

            name_and_id = f"{args[0]}.{args[1]}"
            objects = storage.all()

            for key, value in objects.items():
                if key == name_and_id:
                    new_instance = self.class_name_to_class[class_name](**objects[key])
                    print(new_instance)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an insatnce based on the class name and id
        and save the changes into the JSON file
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = self.search_for_class(args[0]);
        if class_name:
            if class_name:
                if len(args) < 2:
                    print("** instance id missing **")
                    return

            name_and_id = f"{args[0]}.{args[1]}"
            objects = storage.all()
            filtered_objects = {}
            instance_found = False

            for key, value in objects.items():
                if key == name_and_id:
                    instance_found = True
                else:
                    filtered_objects[key] = value
            if instance_found:
                storage.objects(filtered_objects) # replace the __objects with the filtered to effect changes when save
                storage.save()
            else:
                print ("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        objects = storage.all()
        if arg:
            args = arg.split()
            class_name = self.search_for_class(args[0])
            if class_name:
                for key, value in objects.items():
                    name = key.split('.')[0]
                    if name == class_name:
                        new_instance = self.class_name_to_class[class_name](**value)
                        print(new_instance)
        else:
            for key, value in objects.items():
                name = key.split('.')[0]
                new_instance = self.class_name_to_class[name](**value)
                print(new_instance)


    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        The changes are then saved the the JSON file
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = self.search_for_class(args[0])
            if class_name:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    objects = storage.all()
                    updated_objects = {}
                    instance_found = False
                    name_and_id = f"{args[0]}.{args[1]}"
                    for key, value in objects.items():
                        if key == name_and_id:
                            instance_found = True
                    if instance_found:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                for key_name, value_obj in objects.items():
                                    if key_name == name_and_id:
                                        new_val_obj = {
                                                **value_obj,
                                                args[2]: args[3]
                                                }
                                        updated_objects[key_name] = new_val_obj
                                    else:
                                        updated_objects[key_name] = value_obj
                                storage.objects(updated_objects)
                                storage.save()

                    else:
                        print("** no instance found **")

    def search_for_class(self, name):
        for key, value in self.class_name_to_class.items():
            if name == key:
                return key
        print("** class doesn't exist **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

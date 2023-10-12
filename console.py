#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Display prompt"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is encountered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

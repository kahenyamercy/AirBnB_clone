#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter for the AirBnB_clone
    """
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

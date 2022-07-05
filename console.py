#!/usr/bin/python3
"""holbertonschool-AirBnB_clone - contains the entry
point of the command interpreter:"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand - Holberton command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """emptyline - empty line method"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF - call close method when"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

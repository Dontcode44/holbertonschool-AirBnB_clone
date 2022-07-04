#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
"""holbertonschool-AirBnB_clone"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand - Holberton command interpreter"""
    prompt = "(hbnb) "
    def emptyline(self):
        pass
    def do_quit(self, arg):
        """quit - call close method"""
        self.close()
        return True
    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            all_objs = models.storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj)
        elif type(arg) is not __class__:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 3:
            print("** instance id missing **")
        elif arg[2] in models.FileStorage.__objects:
            print("yes")
        
    def close(self):
        """close - exit the program"""
        pass
    def do_EOF(self, arg):
        """EOF - call close method when """
        return True

if __name__ == '__main__':
    """main - executes an interpreter loop"""
    HBNBCommand().cmdloop()
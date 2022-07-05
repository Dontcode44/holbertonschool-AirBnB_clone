#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
"""holbertonschool-AirBnB_clone - contains the entry
point of the command interpreter:"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand - Holberton command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def emptyline(self):
        """emptyline - empty line method"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """create - create method"""
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
        """Function show """
        arg = arg.split()
        all_objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) != 2:
            print("** instance id missing **")
        elif f'BaseModel.{arg[1]}' in all_objs.keys():
            print(arg[1])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based id"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** instance id missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            strs = arg[0] + '.' + arg[1]
            for key, value in objs.items():
                if strs in key:
                    del objs[strs]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        str_ins = arg.split()
        all_objs = models.storage.all()
        if not arg or str_ins[0] in HBNBCommand.classes:
            str_rep = []
            for obj in all_objs.values():
                str_rep.append(obj.__str__())
                print("str_rep")
            else:
                print("** class doesn't exist **")

    def do_EOF(self, arg):
        """EOF - call close method when """
        return True


if __name__ == '__main__':
    """main - executes an interpreter loop"""
    HBNBCommand().cmdloop()

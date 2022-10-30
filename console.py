#!/usr/bin/python3
"""Console module"""
import cmd
import models
from models.base_models import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

cls_arr = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """Method to handle EOF to exit program"""
        print()
        exit()

    def do_quit(self, command):
        """Method to exit console"""
        exit()

    def help_EOF(self):
        """Prints the help documentations for EOF"""
        print("Exit the program")
    
    def help_quit(self):
        """prints the help doc for quit"""
        print("Exits the program with formatting")

    def emptyline(self):
        """Overwriting the  emptyline method"""
        pass


    def do_create(self, args):
        """Creates a new instance"""
        if arg:
            if arg in HBNBCommand.cls_arr:
                class_to_ins = HBNBCommand.cls_arr.get(arg)
                new_inst = class_to_ins()
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls_arr.key():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all().key():
            print("** instance id missing **")
        else:
            obj = models.storage.all().get(args[0] + "." + args[1])


    def do_destroy(self,args):
        """Deletes an instance based on the class and id"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(args[0] + "." + args[1], None)
            models.storage.save()

    
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        string = ""
        lst_all = []
        if arg == "":
            for key, value in models.storage.all().items():
                string = str(value)
                lst_all.append(string)
            print(lst_all)
        elif args[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == args[0]:
                    string = str(value)
                    lst_all.append(string)
            print(lst_all)


    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif args[0] + "." + args[1] not in models.storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = models.storage.all().get(args[0] + "." + args[1])
            setattr(obj, args[2], args[3][1:-1])
            obj.save()
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()


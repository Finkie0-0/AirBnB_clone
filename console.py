#!/usr/bin/python3
"""Console module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt: '(hbnb)'

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()


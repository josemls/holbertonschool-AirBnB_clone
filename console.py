#!/usr/bin/python3
"""
Creating the command interpreter console
"""
import models
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage



class HBNBCommand(cmd.Cmd):
    """
    Class Command interpreter
    """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def do_quit(self, line):
        """Quits command that exits the program """
        exit()
    
    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line not in CLASSES:
                print("** class doesn't exist **")
            else:
                str = line + "()"
                base_inst = eval(str)
                base_inst.save()
                print(base_inst.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
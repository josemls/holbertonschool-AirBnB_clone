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
from models.base_model import BaseModel

classes = {"Amenity": Amenity, "BaseModel": BaseModel,
              "City": City, "Place": Place, "Review": Review,
              "State": State, "User": User}



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
        try:
            str = line + "()"
            instance = eval(str)
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")
    
    def do_show(self, line):
        arg_list = line.split()
        object_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif arg_list[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
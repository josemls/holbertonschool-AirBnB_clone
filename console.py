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
        args_list = line.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

        def do_destroy(self, line):
            """Destroys all items"""
            args = line.split()
            obj_dict = storage.all()

            if not line:
                print("** class name missing **")
                return
            elif not args[0] or args[0] not in classes:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            instance_key = "{}.{}".format(args[0], args[1])
            if instance_key not in obj_dict:
                print("** no instance found **")
                return
            else:
                del obj_dict[instance_key]
            storage.save()         
        
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
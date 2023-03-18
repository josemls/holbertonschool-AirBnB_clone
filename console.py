#!/usr/bin/python3
"""
Creating the command interpreter console
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
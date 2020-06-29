#!/usr/bin/python3
'''Method Command Interpreter'''

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        raise SystemExit

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def do_help(self, args):
        '''help'''
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

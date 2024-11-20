#!/usr/bin/python3
import cmd


class manage_user(cmd.Cmd):

    """Simple command line interpreter for managing users"""

    prompt = 'Airbnb clone console$ '

    def __init__(self):
        super().__init__()
        self.users = {}

    def do_create(self, line):
        """creates a new user"""
        args = line.split()
        if len(args) == 2:
            number, name = args
            self.users[value] = name
            print(f"New User - ID: {number}, Name: {name}")
        else:
            print("wrong input")

    def do_read(self, line):
        """read and display all users"""
        print("user list")
        for number, name in self.users.items():
            print(f"ID: {number}, Name: {name}")

    def do_EOF(self, line):
        """Exits the console"""
        print()
        return True

    def do_update(self, line):
        """updats the users name using a syntax"""
        args = line.split()
        if len(args) == 2:
            number, name = args
            if number in self.users:
                self.users[number] = name
                print(f"update user - ID: {number}, Name: {name}")
            else:
                print("No user found - ID: {number}")
        else:
            print("Wrong input")

    def do_destroy(self, line):
        if line in self.users:
            del self.users[line]
            print(f"Deleted User - ID: {line}")
        else:
            print(f"No user deleted - ID: {line}")

    def default(self, line: str):
        print(f"command unknown: {line}")

    def emptyline(self):
        print("this line is empty")

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    manage_user().cmdloop()

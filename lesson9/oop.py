#OOP

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

user1 = User("John", 27)
user1.print_name()
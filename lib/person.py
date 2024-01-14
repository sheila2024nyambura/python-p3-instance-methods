#!/usr/bin/env python3

class Person:
    def greet(self, name, age):
        return f"Hello, my name is {name} and I am {age} years old."

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

person_instance = Person()

person_instance.walk()

person_instance.talk()

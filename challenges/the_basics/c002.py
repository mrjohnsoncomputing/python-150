from __future__ import annotations
from dataclasses import dataclass

# Ask for the user's first name and then ask for their surname 
# and display the output message "Hello [First Name] [Surname]"

def beginner():
    # This is a tribute to bad code
    print(
        "Hello", 
        input("What is your first name?"), 
        input("What is your surname?")
    )

@dataclass
class Person:
    first_name: str
    surname: str

    @classmethod
    def from_user_input(cls):
        print("What is your first name?")
        name = input("First Name: ")
        print("What is your surname?")
        last_name = input("Surname: ")
        return cls(
            first_name=name,
            surname=last_name
        )

    def greet(self, person: Person):
        print(f"{self} says: 'Hello {person}'")

    def __str__(self) -> str:
        return f"{self.first_name} {self.surname}".title()

def medium():
    user = Person.from_user_input()
    print("Hello {0} {1}".format(
        user.first_name,
        user.surname
    ))

class PersonBuilder:
    def __init__(self):
        self._first_name = ""
        self._surname = ""

    def with_user_input_first_name(self):
        print("What is your first name?")
        self._first_name = input("First Name: ")
        return self

    def with_user_input_surname(self):
        print("What is your surname?")
        self._surname = input("Surname: ")
        return self

    def build(self) -> Person:
        return Person(first_name=self._first_name, surname=self._surname)


def advanced():
    receptionist = Person(first_name="Steven", surname="Smith")

    person_builder = PersonBuilder()
    user = person_builder \
        .with_user_input_first_name() \
        .with_user_input_surname() \
        .build()
    
    receptionist.greet(person=user)
    user.greet(person=receptionist)
    
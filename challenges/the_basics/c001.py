from dataclasses import dataclass

# Ask for the user's first name and display the output message "Hello [First Name]"

def beginner():
    name = input("What is your first name?")
    print("Hello " + name)

@dataclass
class Person:
    first_name: str

    @classmethod
    def from_user_input(cls):
        print("What is your first name?")
        first_name = input("First Name: ")
        return cls(
            first_name=first_name
        )

    def __str__(self) -> str:
        return self.first_name.lower().capitalize()

def medium():
    person = Person.from_user_input()
    print(f"Hello {person.first_name}")

class Greeter:
    def __init__(self, greeting: str):
        self._greeting = greeting

    def greet_person(self, person: Person):
        print(f"{self._greeting} {person}")

def advanced():
    user = Person.from_user_input()
    greeter = Greeter(greeting="Hello")
    greeter.greet_person(person=user)
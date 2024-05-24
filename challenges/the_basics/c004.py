from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Ask the user to enter two numbers.
# Add them together and display the answer as "The total is [answer]"

def beginner():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    print(f"The total is {num1 + num2}")

class UserInput:
    def get_integer(self, message: str, label: str = "Number") -> int:
        print(message)
        valid_response = False

        while not valid_response:
            response = input(f"{label}: ")
            try:
                number = int(response)
                valid_response = True
            except:
                print("Invalid integer - please enter a whole number")
        return number

def medium():
    user_input = UserInput()
    number1 = user_input.get_integer("Please enter a number")
    number2 = user_input.get_integer("Please enter a second number")
    print(f"The total is {number1 + number2}")

class Calculation(ABC):
    @abstractmethod
    def calculate(self, number_pair: NumberPair) -> CalculationResult:
        raise NotImplementedError()
    
class Addition(Calculation):
    def calculate(self, number_pair: NumberPair) -> CalculationResult:
        addition_result = number_pair.number1 + number_pair.number2
        return CalculationResult(result=addition_result)

@dataclass
class NumberPair:
    number1: float = 0 
    number2: float = 0

    @classmethod
    def from_user_input(cls, user_input: UserInput):
        number1 = user_input.get_integer("Please enter the first number")
        number2 = user_input.get_integer("Please enter the second number")
        return cls(
            number1=number1,
            number2=number2
        )

@dataclass
class CalculationResult:
    result: float

    def display(self):
        print(f"The total is {self.result}")

def advanced():
    number_pair = NumberPair.from_user_input(user_input=UserInput())
    adder = Addition()
    result = adder.calculate(number_pair=number_pair)
    result.display()
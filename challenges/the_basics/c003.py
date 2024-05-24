from dataclasses import dataclass
import json
from pathlib import Path
from csv import DictReader
from time import sleep

# Write code that will display the joke "What do you call a bear with no teeth?"
# and on the next line display the answer "A gummy bear!"
# Try to create it using only one line of code

def beginner():
    print("What do you call a bear with no teeth?\nA gummy bear!")

@dataclass
class Joke:
    setup: str
    punchline: str

    def tell(self):
        print(self.setup)
        input()
        print(self.punchline)

def medium():
    Joke(setup="What do you call a bear with no teeth?", punchline="A gummy bear!").tell()

class JokeFactory:
    def _jokes_from_dict(self, data: dict[str, str]) -> list[Joke]:
        jokes = []
        for dictionary in data:
            joke = Joke(setup=dictionary["setup"], punchline=dictionary["punchline"])
            jokes.append(joke)
        return jokes

    def get_jokes_from_file(self, file_path: Path) -> list[Joke]:
        file_type = file_path.suffix
        if file_type == ".csv":
            return self.get_jokes_from_csv(file_path=file_path)
        elif file_type == ".json":
            return self.get_jokes_from_json(file_path=file_path)
        else:
            raise ValueError(
                f"Unsupported file type - {file_type} - from file path {file_path.as_posix()}"
                + "\nPlease supply either a .csv file or a .json file")

    def get_jokes_from_csv(self, file_path: Path) -> list[Joke]:
        with open(file_path, "r") as f:
            reader = DictReader(f)
            converted_data = list(reader)
        return self._jokes_from_dict(data=converted_data)
        
    
    def get_jokes_from_json(self, file_path: Path) -> list[Joke]:
        with open(file_path, "r") as f:
            converted_data = json.load(f)
        return self._jokes_from_dict(data=converted_data)

class Comedian:
    def __init__(self, name: str) -> None:
        self._name = name

    def tell_joke(self, joke: Joke):
        print(joke.setup)
        sleep(1)
        print(joke.punchline)

    def tell_jokes(self, jokes: list[Joke]):
        print("LADIES AND GENTLEMEN")
        print("Please welcome to the stage - the wonderful")
        print(f"##### {self._name} #####\n\n")
        for i in range(len(jokes)):
            self.tell_joke(jokes[i])
            if i < len(jokes) - 1:
                print("Would you like to hear another joke?")
                answer = input("y/n: ").lower()
                if answer != "y":
                    break

def advanced():
    file_path = Path("./challenges/the_basics/jokes/jokes.txt")
    jokes = JokeFactory().get_jokes_from_file(file_path=file_path)
    Comedian("Samantha Giggles").tell_jokes(jokes)
    

from asyncio.windows_events import NULL
import random

def loadAffirmations(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: affirmations.txt not found")
        return NULL

def getRandomAffirmation(affirmations, lastAffirmation=None):
    if not affirmations:
        return "No affirmations available"

    if len(affirmations) == 1:
        return affirmations[0]

    newAffirmation = random.choice(affirmations)
    while newAffirmation == lastAffirmation:
        newAffirmation = random.choice(affirmations)
    return newAffirmation

def main():
    affirmations = loadAffirmations("affirmations.txt")
    if not affirmations:
        return

    print("Welcome to your Daily Affirmations App!")

    lastAffirmation=None
    while True:
        userInput = input("Press Enter for an affirmation or q to quit: ")
        if userInput.lower() == 'q':
            print("Goodbye! Have a lovely day!")
            break
        affirmation = getRandomAffirmation(affirmations, lastAffirmation)
        print("\nYour affirmation for today:")
        print(f"{affirmation}\n")
        lastAffirmation = affirmation

if __name__ == "__main__":
    main()
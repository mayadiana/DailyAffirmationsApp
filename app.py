from doctest import debug
from flask import Flask, render_template
import random

app = Flask(__name__)

def loadAffirmations(filename="affirmations.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ["No affirmations found."]

@app.route("/")
def home():
    affirmations = loadAffirmations()
    affirmation = random.choice(affirmations)
    return render_template("index.html", affirmation=affirmation)

if __name__ == "__main__":
    app.run(debug=True)
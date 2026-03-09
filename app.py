from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

LMStudioURL = "http://localhost:1234/v1/chat/completions"

EmotionsList = [
    {"name": "Happy", "emoji": "😊"},
    {"name": "Sad", "emoji": "😢"},
    {"name": "Anxious", "emoji": "😟"},
    {"name": "Grateful", "emoji": "🙏"},
    {"name": "Tired", "emoji": "😴"},
    {"name": "Hopeful", "emoji": "✨"}
]

def loadAffirmations(filename="affirmations.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ["No affirmations found."]

def generatePersonalizedAffirmation(emotion):
    prompt = (
        f"You are a helpful assistant who ONLY generates affirmations. Your goal is to create a unique, "
        f"personalized, and positive affirmation that directly reflects the user's stated feeling and situation. "
        f"DO NOT include any explanations or extra commentary. ONLY output the affirmation.\n\n"
        f"Here are some examples of good affirmations:\n"
        f"User's Feeling: sad\n"
        f"Affirmation: My sadness is a valid emotion, and I give myself the space and grace to feel it fully.\n"
        f"User's Feeling: furious\n"
        f"Affirmation: I can channel this intense energy into productive and positive action.\n"
        f"User's Feeling: I'm feeling overwhelmed at work and don't know where to start.\n"
        f"Affirmation: I am capable of managing my tasks. I will focus on one small step at a time, and every step is progress.\n"
        f"User's Feeling: feeling lost\n"
        f"Affirmation: I trust that I am on the right path, even if I cannot see the next step clearly.\n\n"
        f"---\n"
        f"Now, generate a new, unique affirmation for the following user feeling. "
        f"Base the affirmation on the entire situation, not just one word. "
        f"Avoid generic phrases like 'I am capable of navigating this feeling'.\n"
        f"User's Feeling: {emotion}\n"
        f"Affirmation:"
    )
       
    payload = { 
        "model": "google/gemma-3-12b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.9, 
        "top_p": 0.9 
    }

    try:
        response = requests.post(LMStudioURL, json=payload, timeout=30)

        if response.status_code == 200:
            data = response.json()  
            reply = data["choices"][0]["message"]["content"].strip().strip('"')
            return reply    
        else:
            return "The AI assistant had a problem generating a response. Please try again."
    except requests.exceptions.RequestException:
        return "Could not connect to the AI assistant. Please ensure LM Studio is running."

@app.route("/", methods=["GET", "POST"])
def home():
    affirmation = ""
    if request.method == "POST":
        if 'feeling' in request.form and request.form['feeling']:
            userFeeling = request.form.get("feeling")
            affirmation = generatePersonalizedAffirmation(userFeeling)
        elif 'emotionChoice' in request.form:
            selectedEmotion = request.form.get("emotionChoice")
            affirmation = generatePersonalizedAffirmation(selectedEmotion)
        else: 
            affirmations = loadAffirmations() 
            affirmation = random.choice(affirmations)
    else: 
            affirmations = loadAffirmations() 
            affirmation = random.choice(affirmations)
    
    return render_template("index.html", affirmation=affirmation, emotions=EmotionsList)

if __name__ == "__main__":
    app.run(debug=True)

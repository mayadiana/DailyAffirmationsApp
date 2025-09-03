import os
import requests

#using an API KEY
#API_KEY = "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"
#print("DEBUG API_KEY:", API_KEY)
#url = "https://openrouter.ai/api/v1/chat/completions"

#using a local server
url = "http://192.168.1.112:1234/v1/chat/completions"

print("Welcome to the Daily Affirmations Console!\n If you want a different affirmation based on your emotion, type 'another'. Type 'exit' to quit.")
print("Describe how you're feeling: ")

currentEmotion = None
lastAffirmation = ""

while True:
    userInput = input("> ").strip()

    if userInput.lower() == "exit":
        print("Until next time!")
        break

    if userInput.lower() == 'another':
        if not currentEmotion:
            print("You haven't described an emotion yet. Please enter how you're feeling.")
            continue
        emotion = currentEmotion
    else:
        emotion = userInput
        currentEmotion = emotion
        lastAffirmation = ""

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
            #API KEY
            #"model": "meta-llama/llama-3.3-8b-instruct:free",

            #local server
            "model": "google/gemma-3-12b",
            
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.9, # Added to encourage variety
            "top_p": 0.9 #also for variety
        }

        #API KEY
        #headers = {
        #    "Authorization": f"Bearer {API_KEY}"
        #}

        #API KEY
        #response = requests.post(url, json=payload, headers=headers)

    #local server
    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()  
            reply = data["choices"][0]["message"]["content"].strip()

            maxAttempts = 3
            attempts = 0

            while reply == lastAffirmation and attempts < maxAttempts:
                response = requests.post(url, json=payload)
                data = response.json()
                reply = data["choices"][0]["message"]["content"].strip()
                attempts += 1

            last_affirmation = reply
            print("Assistant:", reply)          
        else:
            print("Error: ", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"\nError connecting to LM Studio server: {e}")
        print("Please ensure LM Studio is running and the server has been started.")
        break
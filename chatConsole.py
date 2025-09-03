import os
import requests

#using an API KEY
API_KEY = "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"
#print("DEBUG API_KEY:", API_KEY)
url = "https://openrouter.ai/api/v1/chat/completions"

#using a local server
#url = "http://192.168.1.105:1234/v1/chat/completions"

print("Welcome to the Daily Affirmations Console! Type 'exit' to quit.")
print("Describe how you're feeling: ")

currentEmotion = None

while True:
    userInput = input("")
    if userInput.lower() == "exit":
        print("Until next time!")
        break
    if userInput.lower() == "another":
        if not currentEmotion:
            print("You haven't described an emotion yet. Please enter how you're feeling.")
            continue
        emotion = currentEmotion
    else:
        emotion = userInput
        currentEmotion = emotion
        prompt = ( 
            f"You are a helpful assistant who ONLY generates affirmations.\n"
            f"Given the emotion the user is feeling: {emotion}, generate a personalized, positive affirmation." 
            f"DO NOT include any explanations, analysis, or extra commentary.\n"
            f"ONLY output the affirmation, nothing else, not your thoughts or analysis."      
            )

        payload = { 
            #API KEY
            "model": "meta-llama/llama-3.3-8b-instruct:free",

            #local server
            #"model": "openai/gpt-oss-20b",

            "messages": [{"role": "user", "content": prompt}]
        }

        #API KEY
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        #API KEY
        response = requests.post(url, json=payload, headers=headers)

    #local server
    #response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()  
        reply = data["choices"][0]["message"]["content"]
        print("Assistant: ", reply)             
    else:
        print("Error: ", response.status_code, response.text)
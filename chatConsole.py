import os
import requests

#using an API KEY
#API_KEY = "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"
#print("DEBUG API_KEY:", API_KEY)
#url = "https://openrouter.ai/api/v1/chat/completions"

#using a local server
url = "http://192.168.1.105:1234/v1/chat/completions"

print("Welcome to the Daily Affirmations Console! Type 'exit' to quit.")

while True:
    emotion = input("Describe how you're feeling: ")
    if emotion.lower() == "exit":
        print("Until next time!")
        break

    prompt = f"I am feeling {emotion}. Generate me a personalized, positive affirmation based on this emotion."

    payload = { 
        #"model": "openai/gpt-oss-20b:free",
        "model": "openai/gpt-oss-20b",
        "messages": [{"role": "user", "content": prompt}]
    }

    #headers = {
    #    "Authorization": f"Bearer {API_KEY}"
    #}

    #response = requests.post(url, json=payload, headers=headers)
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()  
        reply = data["choices"][0]["message"]["content"]
        print("Assistant: ", reply)
    else:
        print("Error: ", response.status_code, response.text)
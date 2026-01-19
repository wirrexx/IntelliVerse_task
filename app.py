from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")



def call_mistral_api(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions "
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
        }
    
    payload = {
        "model":"mistral-small-latest",
        "message": [{"role": "user", "content": prompt}]
        }
    
    # send a post request to url, 
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
    

   
def call_openroute_api(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://pythonanywhere.com",
        "X-Title": "Simple Chatbot Demo",
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]



@app.route("/", methods=["GET", "POST"])
def index():
    # create the logic to call on the apis here
    return render_template ("index.html")


if __name__ == "__main__":
    app.run(debug=True)
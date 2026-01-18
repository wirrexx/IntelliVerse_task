from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
OPENROUTE_API_KEY = os.getenv("OPENROUTE_API_KEY")



def call_mistral_api(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions "
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
        }
    
    payload = {
        "model":"mistral-large-latest",
        "message": [{"role": "user", "content": prompt}]
        }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
    

   
def call_openroute_api(prompt: str) -> str:
    # query OpenRoute API
    pass



@app.route("/")
def index():
    return render_template ("index.html")


if __name__ == "__main__":
    app.run(debug=True)
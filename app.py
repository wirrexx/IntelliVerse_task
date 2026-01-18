from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
OPENROUTE_API_KEY = os.getenv("OPENROUTE_API_KEY")

def call_mistral_api(prompt: str) -> str:
    # query Mistral API
    pass

def call_openroute_api(prompt: str) -> str:
    # query OpenRoute API
    pass



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)
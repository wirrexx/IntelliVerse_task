import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": "Hello!"}],
    },
)

print("MISTRAL_API_KEY:", os.getenv("OPENROUTER_API_KEY"))
print(response.json())
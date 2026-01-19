import os
import requests

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": "Hello!"}],
    },
)

print("MISTRAL_API_KEY:", os.getenv("MISTRAL_API_KEY"))
print(response.json())
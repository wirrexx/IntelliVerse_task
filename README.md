# IntelliVerse_task
Roman task: Deploy on PythonAny. a simple chatbot 
Whats asked?
- Create a simple chatbot
- Using API and multiple LLM providers (Mistral and OpenRouter)
- Return model answers via Basic UI (Jinja? basic html?)
- Share a Link on Telegram to @rmant7

Whats not being asked!
-  A mobile App
-  Fancy UI
-  Conversation Memory
-  Authentication


KISS: 
- Backend: Python + Flask
- FrontEnd: simple html (Jinja)
- Deploy Pythonanywhere!

How to keep it simple?
- Single Page with Text Input / User prompt
- Dropdown menu 1. Mistral 2. OpenROuter
- Submit Button
- Response display

Backend Logic: 

User submits prompt + model choice
↓
Flask route receives request
↓
If model == "mistral":
    call Mistral API
Else if model == "openrouter":
    call OpenRouter API
↓
Return response text
↓
Render it in HTML


## Topics to Read about:
Requests (Pip install)
https://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

## TODO 

- [x] create virtual environment
- [x] Install flask
- [x] check if flask is installed and working
- [x] create a simply route 
- [x] create a templates folder
- [x] create index.html
- [x] render index.html


- [x] create function for mistral
- [x] create the calls for mistral
    - [x] Read the ChatCompletions in Mistral
    - [x] Implement role, content
    - [x] Implement endpoints
    - [x] test endpoints

    ![Alt text](static/mistral.png)


- [x] create function for openrouter
- [x] create the calls for OpenRoute
    - [x] Read the Doc OpenRoute
    - [x] Implement role, content
    - [x] Implement endpoints
    - [x] test endpoints
    ![Alt text](static/openrouter.png)

## !! Remember, Mistral curl and Openroute similiar ways to connect to the API data.!! 
---------------------------------------------------------
# Post Mortem Notes
#### What was hard?
- Figuring out Curl and Json configuration
- using Requests library 
- Figuring out how to export the env. keys that i generated on Mistral and OpenRouter

# Steps to create the app:
1. Set up Virtual environment
2. Activate Venv
3. Install flask 
4. create app.py (make sure this is in the right place)
!! first error !!
Python did not choose the right interpreter, needed to reselect it!
5. remember to add if __name__== ("__main__"): to it's easier to python3 app.py run the file!
6. add a simple @app.route("/") 
7. create an index function and only return "hello world"
8. import os to getenv API keys.
9. Make sure that you already have created two keys.
10. two variables MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY") and OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY)

------------------------------------------------------
11. Create first function for texting, the curl on mistral API doc website shows you whats needed.
- url = "https://api.mistral.ai/v1/chat/completions"
- Post = headers = key:value, headers = {'Authorization: Bearer YOUR_APIKEY_HERE', 'Content-Type: application/json'}

12. payload ={"model":mistral-small-latest","message" = [{"role":"user", "content":prompt}]}
13. pip install Requests
14. import requests
15. response = requests.post(url, header, json=payload)
16. response.raise_for_status() (raise http error if one occurs)
17. data = response.json() Decodes json body to python 
18. return data["choices"][0]["message"]["content"]



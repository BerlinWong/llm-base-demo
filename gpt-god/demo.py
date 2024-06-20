import os

import requests
from dotenv import load_dotenv

load_dotenv()
# sk-Z6ypjwFE0NVxQJ7f6fwdEtbqal2w5mqxlndLBUhIMjtO3FfC
GPT_GOD_API_KEY = os.getenv("GPT_GOD_API_KEY")
url = "https://api.gptgod.online/v1/chat/completions"
headers = {
    "Authorization": f'Bearer {GPT_GOD_API_KEY}',
    "Content-Type": "application/json"
}
data = {
    "model": "glm-4-flash",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())

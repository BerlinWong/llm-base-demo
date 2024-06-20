# GPTGOD

```shell
import requests

url = "https://api.gptgod.online/v1/chat/completions"
headers = {
    "Authorization": "Bearer YOUR_OPENAI_API_KEY",
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
```

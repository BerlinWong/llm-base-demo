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

密钥：sk-Z6ypjwFE0NVxQJ7f6fwdEtbqal2w5mqxlndLBUhIMjtO3FfC
接口：https://api.gptgod.online/   
模型：glm-4-flash 支持联网     
模型名：net-glm-4-flash     
20亿token，rpm：100    
6.19记录，还剩17.6亿token     
[直达帖子](https://linux.do/t/topic/114286)

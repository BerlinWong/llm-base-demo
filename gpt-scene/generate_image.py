import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取 OpenAI API 密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def generate_image(prompt):
    url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
        'n': 1,
        'size': '256x256',
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    prompt = "一个在田野间放风筝的小姑娘，整体是一个漫画风，给人一种朝气蓬勃心生的向往的感觉，准备用来做我们网站的用户头像。"
    try:
        result = generate_image(prompt)
        image_url = result['data'][0]['url']
        print(f"Generated image URL: {image_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

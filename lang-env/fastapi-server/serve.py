#!/usr/bin/env python
from typing import List
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

from dotenv import load_dotenv

load_dotenv()

# 读取LangSmith Key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "lang-env"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# 使用GPT_GOD
GPT_GOD_API_KEY = os.getenv("GPT_GOD_API_KEY")
# 1. 创建提示模板
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])
# 2. 创建模型
model = ChatOpenAI(model="glm-4-flash",
                   base_url="https://api.gptgod.online/v1/",
                   api_key=GPT_GOD_API_KEY
                   )
# 3. 创建解析器
parser = StrOutputParser()
# 4. 创建链
chain = prompt_template | model | parser
# 4. 应用程序定义
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)
# 5. 添加链路由
add_routes(
    app,
    chain,
    path="/chain",
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

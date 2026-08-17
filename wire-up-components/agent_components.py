import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

model = "openai/gpt-4.1-mini"
messages = []

messages = [
    {
        "role": "system",
        "content": "You are a helpful personal assistant. Use your tools when you need real data."
    }
]

while True:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    finish_reason = response.choices[0].finish_reason
    if finish_reason == "stop":
        print(response.choices[0].message.content)
        break

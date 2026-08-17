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

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check the user's calendar for events on a given date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date to check, e.g. 2026-03-14"
                    }
                },
                "required": ["date"]
            }
        }
    }
]

def check_calendar(date):
    return "10am: Team standup, 2pm: Dentist appointment"

while True:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    finish_reason = response.choices[0].finish_reason
    if finish_reason == "stop":
        print(response.choices[0].message.content)
        break

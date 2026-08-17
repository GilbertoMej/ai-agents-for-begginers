import os
import json
from openai import OpenAI
from tools import check_calendar, search_web, get_user_preferences, TOOLS_SCHEMA

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

MAX_ITERATIONS = 10

system_prompt = """You are a helpful personal assistant.
Use your tools to find information when needed.
Before calling a tool, use 'Thought:' to explain your reasoning.
After a tool result, use 'Observation:' to note what you learned.
Provide clear, concise answers."""

def run_agent(user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    # Add the agent loop here


import os, json
from openai import OpenAI
from tools import tools, execute_tool

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

SYSTEM_PROMPT = "You are a helpful personal assistant. Use your tools when you need real data."

def run_agent(messages):
    while True:
        response = client.chat.completions.create(
            model="openai/gpt-4.1-mini",
            messages=messages,
            tools=tools,
        )
        choice = response.choices[0]
        messages.append(choice.message)
        if choice.finish_reason == "tool_calls":
            for tc in choice.message.tool_calls:
                args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                result = execute_tool(tc.function.name, args)
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
        else:
            return choice.message.content

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

questions = [
    "What's on my calendar today?",
    "Tell me about the standup.",
    "What time is my dentist?",
    "Am I free at 3pm?",
    "Summarise my day.",
]

for q in questions:
    messages.append({"role": "user", "content": q})
    answer = run_agent(messages)
    print(f"Q: {q}")
    print(f"A: {answer}")
    print(f"Messages in history: {len(messages)}")
    print()


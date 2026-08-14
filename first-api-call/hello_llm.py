import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

prompt = "Write a one-sentence story about a robot."

print(f"{'─'*90}")
print(f"{'temp=0.0':<45} {'temp=2.0':<45}")
print(f"{'─'*90}")

for i in range(10):
    r0 = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}]
    )
    r2 = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=2.0,
        messages=[{"role": "user", "content": prompt}]
    )
    left  = r0.choices[0].message.content.strip()[:43]
    right = r2.choices[0].message.content.strip()[:43]
    print(f"{left:<45} {right:<45}")

print(f"{'─'*90}")
print("\nLeft: deterministic  -  same answer every run")
print("Right: random  -  different answer every run")

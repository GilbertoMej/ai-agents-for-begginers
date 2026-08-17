# import python SDK
from openai import OpenAI

# Create client
client = OpenAI(
    base_url="YOUR_BASE_URL",
    api_key="YOUR_API_KEY"
)

# First API Call
response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    messages=[
        {"role": "system",
         "content": "Be concise and friendly."},
        {"role": "user", "content": "What is an AI agent?"}
        ]
)

print(response.choices[0].message.content)

import os
from openai import OpenAI


client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.getenv('DEEPSEEK_API_KEY'),
)


completion = client.chat.completions.create(
  model="deepseek-chat",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=False,
)

print(completion)

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # 🔥 THIS was missing

client = OpenAI(
    api_key=os.getenv("YOUR_OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def ask_ai(text):
    response = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
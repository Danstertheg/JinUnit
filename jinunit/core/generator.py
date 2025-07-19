import os
from openai import OpenAI
from dotenv import load_dotenv
from .prompts import TEST_PROMPT
from pathlib import Path

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("API Key:", os.getenv("OPENAI_API_KEY"))
def generate_test(file_path: Path) -> str:
    code = file_path.read_text()
    prompt = TEST_PROMPT.format(code=code)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Java testing expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1500,
    )

    return response.choices[0].message.content
import ollama
import json
import re

async def get_ollama_reply(prompt: str) -> list:
    response = ollama.chat(
        model="llama3.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    raw_text = response["message"]["content"].strip()

    match = re.search(r"```(?:json)?\n([\s\S]*?)```", raw_text)
    if match:
        json_text = match.group(1).strip()
        try:
            replies = json.loads(json_text)
            if isinstance(replies, list):
                return replies
        except json.JSONDecodeError:
            pass

    try:
        replies = json.loads(raw_text)
        if isinstance(replies, list):
            return replies
    except json.JSONDecodeError:
        pass

    return [raw_text]



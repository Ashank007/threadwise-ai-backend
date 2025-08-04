from prompt import build_prompt_generate, build_prompt_analyze
from providers.openai_provider import get_openai_reply
from providers.gemini_provider import get_gemini_reply
from providers.ollama_provider import get_ollama_reply
import os
import re
import json

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama").lower()

async def generate_reply(thread, role, tone,api_key,new_message=None, mode="generate"):
    if mode == "generate":
        prompt = build_prompt_generate(thread, role, tone)
    elif mode == "analyze":
        if not new_message:
            raise ValueError("new_message is required for analyze mode")
        prompt = build_prompt_analyze(thread, new_message, role, tone)
    elif mode == "both":
        prompt = build_prompt_generate(thread, role, tone)
    else:
        raise ValueError("Invalid mode")

    if MODEL_PROVIDER == "openai":
        raw_reply = await get_openai_reply(prompt)
    elif MODEL_PROVIDER == "gemini":
        raw_reply = await get_gemini_reply(prompt,api_key)
    elif MODEL_PROVIDER == "ollama":
         return await get_ollama_reply(prompt)
    else:
        raise ValueError("Unknown MODEL_PROVIDER")

    try:
        # Remove markdown wrappers like ```json
        cleaned = re.sub(r"```json|```", "", raw_reply).strip()

        # Try to parse into list
        replies = json.loads(cleaned)
        if not isinstance(replies, list):
            raise ValueError("Expected a list of replies")
    except Exception as e:
        raise ValueError(f"Failed to parse model reply: {str(e)}\nRaw: {raw_reply}")

    return replies



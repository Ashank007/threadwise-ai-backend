
def build_prompt_generate(thread: str, role: str, tone: str) -> str:
    tone_text = tone.lower() if tone else "neutral"
    role_text = role.lower() if role else "student"
    return (
        f"You are a helpful assistant.\n"
        f"Task: Generate 3 different {tone_text} replies as a {role_text} "
        f"to the following message:\n\"{thread}\"\n\n"
        "Return the replies as a JSON array of strings."
    )


def build_prompt_analyze(thread: str, new_message: str, role: str, tone: str) -> str:
    return f"""
You are a helpful assistant. Analyze the following conversation and continue the reply professionally:

Original email or conversation:
\"\"\"{thread}\"\"\"

New message to analyze:
\"\"\"{new_message}\"\"\"

Write a {tone.lower()} reply as a {role.lower()} continuing the conversation.
"""




def format_gpt_prompt(context):
    """Formats a context string into a GPT-compatible prompt."""
    return f"Explain this archaeological evidence or anomaly in detail: {context}\n\nUse simple language and list key points."

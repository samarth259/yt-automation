from google import genai
import os

def generate_script(topic):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Create a viral YouTube Shorts script (30 seconds) about: {topic}.
    Start with a strong hook.
    """

    response = client.models.generate_content(
        model="gemini-1.0-pro",  # SAFE fallback
        contents=prompt
    )

    return response.text

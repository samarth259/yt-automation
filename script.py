from google import genai
import os

def generate_script(topic):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Create a viral YouTube Shorts script (30 seconds) about: {topic}.
    Make it engaging, fast-paced, and catchy.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text

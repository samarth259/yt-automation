import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script(topic):
    prompt = f"""
    Create a viral YouTube Shorts script (30 seconds) about: {topic}.
    Start with a strong hook in first 3 seconds.
    Make it engaging and fast-paced.
    """

    model = genai.GenerativeModel("models/gemini-pro")

    response = model.generate_content(prompt)

    return response.text

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script(topic):
    prompt = f"""
    Create a viral YouTube Shorts script (30 seconds) about: {topic}.
    Make it engaging, catchy, and fast-paced.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text

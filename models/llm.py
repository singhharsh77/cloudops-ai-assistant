from groq import Groq
from config.config import GROQ_API_KEY

def generate_response(prompt):
    """
    Generates a response using the Groq SDK.
    """
    try:
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM Error: {e}"
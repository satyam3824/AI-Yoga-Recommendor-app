from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Explicitly tell dotenv to load .env file from current directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found. Check your .env file or use hardcoded API key.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_agent_response(user_input: str) -> str:
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

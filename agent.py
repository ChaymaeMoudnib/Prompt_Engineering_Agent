# agent.py - Using NEW google-genai SDK
import os
from dotenv import load_dotenv
from google import genai
from tools import google_search

load_dotenv()

client = genai.Client(api_key=os.getenv("Gemini_api_key"))

def agent_reply(user_prompt: str) -> str:
    if user_prompt.lower().startswith("search "):
        query = user_prompt[len("search "):].strip()
        search_results = google_search(query)
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=f"Summarize the following search results:\n{search_results}"
        )
        return response.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt
    )
    return response.text
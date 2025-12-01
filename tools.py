import os
import requests
from dotenv import load_dotenv

load_dotenv()

serper_key = os.getenv("Serper_api_key")

def google_search(query: str):
    url = "https://google.serper.dev/search"
    headers = {'X-API-KEY': serper_key}
    data = {'q': query}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code != 200:
        return f'Search error. Status code: {response.status_code}'
    
    results = response.json()
    
    summaries = []
    
    for item in results.get('organic', [])[:3]:
        summaries.append(f"- {item.get('title')}:\n  {item.get('snippet')}")
    
    return "\n".join(summaries) if summaries else "No results found."
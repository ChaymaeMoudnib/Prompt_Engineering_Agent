# agent.py - Enhanced with Prompt Engineering Techniques
import os
from dotenv import load_dotenv
from google import genai
from tools import google_search
from prompt_techniques import PromptTechniques

load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("Gemini_api_key"))
pt = PromptTechniques()

def agent_reply(user_prompt: str, technique: str = "zero_shot") -> str:
    """
    Enhanced agent with multiple prompting techniques
    
    Args:
        user_prompt: User's question/request
        technique: Prompting technique to use
            - zero_shot (default)
            - few_shot
            - chain_of_thought (cot)
            - role_based
            - structured
            - emotion
    """
    
    # Handle search requests
    if user_prompt.lower().startswith("search "):
        query = user_prompt[len("search "):].strip()
        search_results = google_search(query)
        
        # Use structured output for search summaries
        prompt = pt.structured_output(
            task=f"Summarize these search results about: {query}",
            format_spec="""
Key Points (3-5 bullet points):
- Point 1
- Point 2
...

Summary (2-3 sentences):
[Your summary here]
"""
        )
        prompt += f"\n\nSearch Results:\n{search_results}"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    # Apply different techniques based on user selection
    final_prompt = user_prompt  # default
    
    if technique == "chain_of_thought" or technique == "cot":
        final_prompt = pt.chain_of_thought(user_prompt)
    
    elif technique == "few_shot":
        # Example for coding tasks
        examples = [
            {
                "input": "Write a function to add two numbers",
                "output": "def add(a, b):\n    return a + b"
            },
            {
                "input": "Write a function to multiply two numbers",
                "output": "def multiply(a, b):\n    return a * b"
            }
        ]
        final_prompt = pt.few_shot(user_prompt, examples)
    
    elif technique == "role_based":
        # Extract role if specified, default to "helpful assistant"
        role = "helpful assistant"
        if "as a" in user_prompt.lower():
            # Try to extract role from user prompt
            parts = user_prompt.lower().split("as a")
            if len(parts) > 1:
                role_words = parts[1].split()[0:3]
                role = " ".join(role_words)
        final_prompt = pt.role_based(role, user_prompt)
    
    elif technique == "structured":
        final_prompt = pt.structured_output(
            user_prompt,
            "Please structure your response clearly with headers and bullet points"
        )
    
    elif technique == "emotion":
        final_prompt = pt.emotion_prompt(user_prompt)
    
    # Generate response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )
    
    return response.text


def demonstrate_techniques(query: str):
    """
    Demonstrate different prompting techniques on the same query
    """
    techniques = {
        "Zero-Shot": "zero_shot",
        "Chain of Thought": "chain_of_thought",
        "Role-Based": "role_based",
        "Emotion Prompt": "emotion"
    }
    
    print(f"\n{'='*60}")
    print(f"Testing Query: {query}")
    print(f"{'='*60}\n")
    
    for name, tech in techniques.items():
        print(f"\n--- Using {name} Technique ---")
        try:
            response = agent_reply(query, technique=tech)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        print("-" * 60)
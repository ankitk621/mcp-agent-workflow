import os
import sys
import json
import requests
from .common import print_agent_step

GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'

def execute(user_command):
    """The main execution function for the PlannerAgent."""
    print_agent_step("PlannerAgent", f"Received user command: '{user_command}'", is_task=True)
    
    # Load context from the product database
    with open('website/products.json', 'r') as f:
        products = json.load(f)
    
    # MCP Interaction: Query the Model API Server (Gemini)
    print_agent_step("PlannerAgent", "Querying Model API Server (Gemini) to parse command...")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY not found in .env file.")
        sys.exit(1)
        
    try:
        parsed_data = _parse_with_gemini(user_command, products, api_key)
        if "error" in parsed_data:
            print(f"❌ PlannerAgent Error: {parsed_data.get('reason', 'Could not parse command.')}")
            sys.exit(1)
            
        print_agent_step("PlannerAgent", "Command parsed successfully. Creating plan...")
        return parsed_data
    except Exception as e:
        print(f"❌ An error occurred during MCP Interaction: {e}")
        sys.exit(1)

def _parse_with_gemini(command, products, api_key):
    """Helper function to call the Gemini API."""
    product_names = [p['name'] for p in products]
    prompt = f"""
You are the PlannerAgent. Your task is to parse user commands into structured data.
The available products are: {', '.join(product_names)}.
Analyze the following user command: "{command}"
Return a JSON object with "productName" and "newPrice". The price must be a number.
"""
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"responseMimeType": "application/json"}
    }
    response = requests.post(f"{GEMINI_API_URL}?key={api_key}", headers=headers, json=payload)
    response.raise_for_status()
    result_text = response.json()['candidates'][0]['content']['parts'][0]['text']
    return json.loads(result_text)


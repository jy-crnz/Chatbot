#Jay Lawrence C. Cerniaz
#BSIT - 2A
#Date 27/03/2025

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Ensure the API key is available
if not api_key:
    raise ValueError("Error: GEMINI_API_KEY is missing. Check your .env file.")

# Configure the generative AI model
genai.configure(api_key=api_key)

def chat_with_ai(user_input):
    """
    Sends user input to the Gemini AI model and returns the response.
    """
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Using a valid AI model
        response = model.generate_content(user_input)
        return response.text if hasattr(response, "text") else str(response)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("AI Chatbot (type 'exit' to stop)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chatbot...")
            break  # Stop the chatbot loop
        
        response = chat_with_ai(user_input)
        print("AI:", response)

from google import genai
import os
from context_manager import ContextManager
from vector_store import VectorStore
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()

# Initialize Google GenAI client and memory systems
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
memory = ContextManager()
archive = VectorStore()

# Using the validated model ID from a successful diagnostic test
MODEL_ID = "gemini-2.5-flash-preview-09-2025" 

def chat_with_agent(user_input):
    """Orchestrates context retrieval, prompt assembly, and LLM execution."""
    
    # 1. Retrieve relevant facts from long-term memory
    past_facts = archive.recall_relevant(user_input)
    
    # 2. Assemble the 'Hydrated Prompt' (Tri-Tier Memory)
    prompt = f"""
    System: You are a professional assistant. Use the provided context if relevant.
    
    [LONG-TERM CONTEXT]: {past_facts}
    [RECENT HISTORY]: {memory.history}
    
    User Query: {user_input}
    """
    
    # 3. Request generation from Gemini 2.5 Flash
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    
    # 4. Update both short-term history and long-term vector archive
    memory.add_to_history("user", user_input)
    archive.archive_message(str(len(memory.history)), user_input)
    
    return response.text

if __name__ == "__main__":
    print(f"Agent Online (Using {MODEL_ID}). Type 'quit' to exit.")
    while True:
        user_in = input("You: ")
        if user_in.lower() in ['exit', 'quit']: break
        try:
            print(f"Agent: {chat_with_agent(user_in)}")
        except Exception as e:
            print(f"Error: {e}")
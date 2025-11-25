"""
Example usage of the WhatsApp Bot
This script demonstrates how to use the bot components directly
"""

from message_handler import MessageHandler
from groq_client import GroqClient
import os

def example_direct_usage():
    """Example of using the bot components directly"""
    
    print("=== WhatsApp Bot - Example Usage ===\n")
    
    # Initialize message handler
    handler = MessageHandler()
    
    # Example conversations
    test_messages = [
        "Hola",
        "¿Cómo estás?",
        "Necesito ayuda con mi cuenta",
        "Gracias, adiós"
    ]
    
    user_id = "example_user_123"
    
    print("Simulando conversación:\n")
    for i, message in enumerate(test_messages, 1):
        print(f"Usuario: {message}")
        response = handler.process_message(user_id, message)
        print(f"Bot: {response}\n")
        print("-" * 50 + "\n")

def example_groq_client():
    """Example of using Groq client directly"""
    
    print("=== Groq Client - Direct Usage ===\n")
    
    # Make sure GROQ_API_KEY is set
    if not os.getenv('GROQ_API_KEY'):
        print("⚠️  GROQ_API_KEY not found in environment variables")
        print("Please set it in your .env file or export it:")
        print("export GROQ_API_KEY='your_key_here'")
        return
    
    try:
        client = GroqClient()
        
        # Test message
        test_message = "Hola, ¿puedes ayudarme?"
        print(f"Pregunta: {test_message}\n")
        
        response = client.generate_response(
            user_message=test_message,
            system_prompt="Eres un asistente amigable y profesional."
        )
        
        print(f"Respuesta: {response}\n")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. Installed requirements: pip install -r requirements.txt")
        print("2. Set GROQ_API_KEY in .env file")
        print("3. Valid Groq API key")

if __name__ == "__main__":
    print("Choose an example to run:")
    print("1. Direct message handler usage")
    print("2. Groq client direct usage")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == "1":
        example_direct_usage()
    elif choice == "2":
        example_groq_client()
    else:
        print("Invalid choice. Running example 1...")
        example_direct_usage()


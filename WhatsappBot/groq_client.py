"""
Groq API Client
Handles all interactions with Groq API for generating intelligent responses
"""

import os
from groq import Groq
from config import (
    GROQ_API_KEY, 
    GROQ_MODEL, 
    GROQ_MAX_TOKENS, 
    GROQ_TEMPERATURE
)
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GroqClient:
    """Client for interacting with Groq API"""
    
    def __init__(self):
        """Initialize Groq client"""
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        self.max_tokens = GROQ_MAX_TOKENS
        self.temperature = GROQ_TEMPERATURE
        
        logger.info(f"Groq client initialized with model: {self.model}")
    
    def generate_response(self, user_message, system_prompt=None, conversation_history=None):
        """
        Generate a response using Groq API
        
        Args:
            user_message (str): The user's message
            system_prompt (str): System instructions for the AI
            conversation_history (list): Previous messages for context
            
        Returns:
            str: Generated response
        """
        try:
            # Default system prompt
            if system_prompt is None:
                system_prompt = """Eres un asistente virtual amigable y profesional para WhatsApp. 
                Responde de manera clara, concisa y útil. 
                Mantén un tono amigable pero profesional.
                Si no sabes algo, admítelo honestamente.
                Responde en el mismo idioma que el usuario.
                Mantén las respuestas breves pero completas."""
            
            # Build messages array
            messages = [{"role": "system", "content": system_prompt}]
            
            # Add conversation history if available
            if conversation_history:
                for msg in conversation_history[-10:]:  # Last 10 messages for context
                    messages.append(msg)
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Generate response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=False
            )
            
            # Extract and return response
            generated_text = response.choices[0].message.content.strip()
            logger.info(f"Response generated successfully: {len(generated_text)} characters")
            
            return generated_text
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "Lo siento, hubo un error al procesar tu mensaje. Por favor, intenta de nuevo."
    
    def generate_streaming_response(self, user_message, system_prompt=None):
        """
        Generate a streaming response (for real-time updates)
        
        Args:
            user_message (str): The user's message
            system_prompt (str): System instructions for the AI
            
        Yields:
            str: Chunks of the generated response
        """
        try:
            if system_prompt is None:
                system_prompt = """Eres un asistente virtual amigable y profesional para WhatsApp."""
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
            
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            logger.error(f"Error in streaming response: {str(e)}")
            yield "Lo siento, hubo un error al procesar tu mensaje."


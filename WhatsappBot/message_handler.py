"""
Message Handler
Processes incoming messages and determines appropriate responses
"""

import re
import logging
from typing import Optional, Dict, List
from groq_client import GroqClient
from bot_instructions import (
    SYSTEM_PROMPT,
    GREETING_PROMPT,
    QUESTION_PROMPT,
    TECHNICAL_SUPPORT_PROMPT,
    COMPLAINT_PROMPT,
    FAREWELL_PROMPT,
    GREETINGS_BY_LANGUAGE,
    FAREWELLS_BY_LANGUAGE
)
from config import ENABLE_CONTEXT, CONTEXT_MEMORY_SIZE

logger = logging.getLogger(__name__)

class MessageHandler:
    """Handles message processing and response generation"""
    
    def __init__(self):
        """Initialize message handler"""
        self.groq_client = GroqClient()
        self.conversation_context: Dict[str, List[Dict]] = {}  # Store context per user
        
    def detect_language(self, text: str) -> str:
        """
        Simple language detection based on common words
        
        Args:
            text: Input text
            
        Returns:
            str: Language code ('es', 'en', 'pt', etc.)
        """
        text_lower = text.lower()
        
        # Spanish indicators
        spanish_words = ['hola', 'gracias', 'por favor', 'adiós', 'cómo', 'qué', 'dónde']
        # English indicators
        english_words = ['hello', 'thanks', 'please', 'goodbye', 'how', 'what', 'where']
        # Portuguese indicators
        portuguese_words = ['olá', 'obrigado', 'por favor', 'tchau', 'como', 'o que', 'onde']
        
        spanish_count = sum(1 for word in spanish_words if word in text_lower)
        english_count = sum(1 for word in english_words if word in text_lower)
        portuguese_count = sum(1 for word in portuguese_words if word in text_lower)
        
        if spanish_count > english_count and spanish_count > portuguese_count:
            return 'es'
        elif english_count > portuguese_count:
            return 'en'
        elif portuguese_count > 0:
            return 'pt'
        else:
            return 'es'  # Default to Spanish
    
    def classify_message(self, message: str) -> str:
        """
        Classify the type of message
        
        Args:
            message: User message
            
        Returns:
            str: Message type ('greeting', 'question', 'complaint', 'technical', 'farewell', 'general')
        """
        message_lower = message.lower()
        
        # Greetings
        greeting_patterns = [
            r'\b(hola|hi|hello|hey|buenos días|buenas tardes|buenas noches|olá)\b',
            r'\b(saludos|greetings)\b'
        ]
        for pattern in greeting_patterns:
            if re.search(pattern, message_lower, re.IGNORECASE):
                return 'greeting'
        
        # Farewells
        farewell_patterns = [
            r'\b(adiós|bye|goodbye|hasta luego|nos vemos|tchau|até logo)\b',
            r'\b(gracias|thanks|thank you|obrigado)\b.*\b(adiós|bye|goodbye)\b'
        ]
        for pattern in farewell_patterns:
            if re.search(pattern, message_lower, re.IGNORECASE):
                return 'farewell'
        
        # Complaints
        complaint_patterns = [
            r'\b(problema|problem|error|no funciona|doesn\'t work|não funciona)\b',
            r'\b(mal|bad|terrible|horrible|pésimo)\b',
            r'\b(queja|complaint|reclamo)\b'
        ]
        for pattern in complaint_patterns:
            if re.search(pattern, message_lower, re.IGNORECASE):
                return 'complaint'
        
        # Technical support
        technical_patterns = [
            r'\b(cómo|how|como)\b.*\b(hacer|do|fazer|usar|use)\b',
            r'\b(ayuda|help|ajuda|soporte|support)\b',
            r'\b(tutorial|guía|guide|instrucciones|instructions)\b'
        ]
        for pattern in technical_patterns:
            if re.search(pattern, message_lower, re.IGNORECASE):
                return 'technical'
        
        # Questions
        question_patterns = [
            r'\?',  # Contains question mark
            r'\b(qué|what|o que|cual|which|cuándo|when|dónde|where|por qué|why)\b'
        ]
        for pattern in question_patterns:
            if re.search(pattern, message_lower, re.IGNORECASE):
                return 'question'
        
        return 'general'
    
    def get_contextual_prompt(self, message_type: str) -> str:
        """
        Get appropriate prompt based on message type
        
        Args:
            message_type: Type of message
            
        Returns:
            str: Contextual prompt
        """
        prompts = {
            'greeting': GREETING_PROMPT,
            'question': QUESTION_PROMPT,
            'technical': TECHNICAL_SUPPORT_PROMPT,
            'complaint': COMPLAINT_PROMPT,
            'farewell': FAREWELL_PROMPT,
            'general': SYSTEM_PROMPT
        }
        return prompts.get(message_type, SYSTEM_PROMPT)
    
    def update_context(self, user_id: str, role: str, content: str):
        """
        Update conversation context for a user
        
        Args:
            user_id: User identifier
            role: 'user' or 'assistant'
            content: Message content
        """
        if not ENABLE_CONTEXT:
            return
        
        if user_id not in self.conversation_context:
            self.conversation_context[user_id] = []
        
        self.conversation_context[user_id].append({
            "role": role,
            "content": content
        })
        
        # Keep only last N messages
        if len(self.conversation_context[user_id]) > CONTEXT_MEMORY_SIZE * 2:
            self.conversation_context[user_id] = self.conversation_context[user_id][-CONTEXT_MEMORY_SIZE * 2:]
    
    def process_message(self, user_id: str, message: str) -> str:
        """
        Process incoming message and generate response
        
        Args:
            user_id: User identifier
            message: User message
            
        Returns:
            str: Bot response
        """
        try:
            # Detect language
            language = self.detect_language(message)
            
            # Classify message
            message_type = self.classify_message(message)
            logger.info(f"Message classified as: {message_type} (language: {language})")
            
            # Get contextual prompt
            contextual_prompt = self.get_contextual_prompt(message_type)
            
            # Enhanced system prompt with language awareness
            enhanced_prompt = f"{SYSTEM_PROMPT}\n\n{contextual_prompt}\n\nIMPORTANTE: Responde en {language}."
            
            # Get conversation history
            conversation_history = None
            if ENABLE_CONTEXT and user_id in self.conversation_context:
                conversation_history = self.conversation_context[user_id]
            
            # Generate response
            response = self.groq_client.generate_response(
                user_message=message,
                system_prompt=enhanced_prompt,
                conversation_history=conversation_history
            )
            
            # Update context
            self.update_context(user_id, "user", message)
            self.update_context(user_id, "assistant", response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            return "Lo siento, hubo un error al procesar tu mensaje. Por favor, intenta de nuevo."
    
    def get_greeting(self, language: str = 'es') -> str:
        """Get a greeting message in the specified language"""
        greetings = GREETINGS_BY_LANGUAGE.get(language, GREETINGS_BY_LANGUAGE['es'])
        import random
        return random.choice(greetings)
    
    def get_farewell(self, language: str = 'es') -> str:
        """Get a farewell message in the specified language"""
        farewells = FAREWELLS_BY_LANGUAGE.get(language, FAREWELLS_BY_LANGUAGE['es'])
        import random
        return random.choice(farewells)


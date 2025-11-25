"""
Configuration file for WhatsApp Bot
Contains all configuration settings and constants
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-70b-versatile')  # Fast and efficient model
GROQ_MAX_TOKENS = int(os.getenv('GROQ_MAX_TOKENS', '500'))
GROQ_TEMPERATURE = float(os.getenv('GROQ_TEMPERATURE', '0.7'))

# WhatsApp Configuration
WHATSAPP_SESSION_PATH = os.getenv('WHATSAPP_SESSION_PATH', './sessions')
WHATSAPP_QR_PATH = os.getenv('WHATSAPP_QR_PATH', './qr_code.png')

# Bot Configuration
BOT_NAME = os.getenv('BOT_NAME', 'Asistente Virtual')
BOT_LANGUAGE = os.getenv('BOT_LANGUAGE', 'es')  # Default Spanish
ENABLE_LOGGING = os.getenv('ENABLE_LOGGING', 'true').lower() == 'true'
LOG_FILE = os.getenv('LOG_FILE', './logs/bot.log')

# Response Configuration
MAX_RESPONSE_LENGTH = int(os.getenv('MAX_RESPONSE_LENGTH', '1000'))
ENABLE_CONTEXT = os.getenv('ENABLE_CONTEXT', 'true').lower() == 'true'
CONTEXT_MEMORY_SIZE = int(os.getenv('CONTEXT_MEMORY_SIZE', '10'))  # Number of messages to remember

# Rate Limiting
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'true').lower() == 'true'
RATE_LIMIT_MESSAGES = int(os.getenv('RATE_LIMIT_MESSAGES', '20'))  # Messages per minute
RATE_LIMIT_WINDOW = int(os.getenv('RATE_LIMIT_WINDOW', '60'))  # Time window in seconds

# Greeting messages
GREETINGS = [
    "¡Hola! 👋 ¿En qué puedo ayudarte hoy?",
    "¡Buenos días! ¿Cómo puedo asistirte?",
    "¡Hola! Estoy aquí para ayudarte. ¿Qué necesitas?",
    "¡Saludos! ¿En qué puedo ser útil?"
]

# Farewell messages
FAREWELLS = [
    "¡Hasta luego! Que tengas un excelente día. 👋",
    "¡Adiós! Fue un placer ayudarte.",
    "¡Nos vemos pronto! Cualquier cosa, aquí estaré.",
    "¡Hasta la próxima! Cuídate mucho."
]


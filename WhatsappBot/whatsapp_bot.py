"""
WhatsApp Bot Main File
Integrates WhatsApp with Groq AI for intelligent conversations
"""

import os
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client as TwilioClient
from twilio.twiml.messaging_response import MessagingResponse
from message_handler import MessageHandler
from config import (
    WHATSAPP_SESSION_PATH,
    ENABLE_LOGGING,
    LOG_FILE
)

# Configure logging
if ENABLE_LOGGING:
    os.makedirs(os.path.dirname(LOG_FILE) if os.path.dirname(LOG_FILE) else '.', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
else:
    logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Initialize message handler
message_handler = MessageHandler()

# Twilio configuration (alternative method)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', '')

# Option 1: Using Twilio API (for production)
def setup_twilio_bot():
    """Setup bot using Twilio API"""
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER]):
        logger.warning("Twilio credentials not found. Using alternative method.")
        return None
    
    return TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Option 2: Using whatsapp-web.js (Node.js) - requires separate setup
# This is a Python wrapper that can call a Node.js service

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint for receiving WhatsApp messages
    Compatible with Twilio, WhatsApp Business API, or custom integrations
    """
    try:
        # Get incoming message data
        # Format depends on the WhatsApp service provider
        incoming_message = request.form.get('Body', '') or request.json.get('message', '')
        sender = request.form.get('From', '') or request.json.get('from', '')
        
        if not incoming_message:
            logger.warning("Received empty message")
            return jsonify({"status": "error", "message": "Empty message"}), 400
        
        logger.info(f"Received message from {sender}: {incoming_message}")
        
        # Process message and generate response
        response_text = message_handler.process_message(
            user_id=sender,
            message=incoming_message
        )
        
        logger.info(f"Generated response: {response_text[:50]}...")
        
        # Return response (format depends on service provider)
        # For Twilio:
        if request.form.get('From'):
            resp = MessagingResponse()
            resp.message(response_text)
            return str(resp)
        
        # For JSON API:
        return jsonify({
            "status": "success",
            "response": response_text
        })
        
    except Exception as e:
        logger.error(f"Error in webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "WhatsApp Bot",
        "ai_provider": "Groq"
    })

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        "message": "WhatsApp Bot with Groq AI",
        "endpoints": {
            "webhook": "/webhook (POST)",
            "health": "/health (GET)"
        }
    })

# Alternative: Direct WhatsApp integration using whatsapp-web.py
def setup_whatsapp_web():
    """
    Setup using whatsapp-web.py library
    Note: This requires additional setup and may need browser automation
    """
    try:
        from whatsapp_web import WhatsAppWeb
        
        logger.info("Setting up WhatsApp Web integration...")
        
        def on_message_received(message):
            """Callback for received messages"""
            user_id = message.get('from', '')
            text = message.get('body', '')
            
            if text:
                response = message_handler.process_message(user_id, text)
                # Send response back
                # Implementation depends on the library used
        
        # Initialize WhatsApp Web client
        # whatsapp = WhatsAppWeb()
        # whatsapp.on_message(on_message_received)
        # whatsapp.start()
        
        logger.info("WhatsApp Web integration ready")
        
    except ImportError:
        logger.warning("whatsapp-web library not available. Using webhook method instead.")
    except Exception as e:
        logger.error(f"Error setting up WhatsApp Web: {str(e)}")

def main():
    """Main function to start the bot"""
    logger.info("Starting WhatsApp Bot with Groq AI...")
    
    # Try to setup WhatsApp Web (alternative method)
    # setup_whatsapp_web()
    
    # Start Flask server for webhook
    port = int(os.getenv('PORT', 5000))
    logger.info(f"Starting Flask server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    main()


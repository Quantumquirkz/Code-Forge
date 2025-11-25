# WhatsApp Bot con Groq AI

Un chatbot inteligente de WhatsApp impulsado por la API de Groq, diseñado para proporcionar respuestas intuitivas y conversaciones naturales con los usuarios.

## 🤖 Características

- **IA Avanzada**: Utiliza modelos de Groq (Llama 3.1) para respuestas rápidas e inteligentes
- **Respuestas Intuitivas**: Sistema de clasificación de mensajes para respuestas contextuales
- **Multilingüe**: Detección automática de idioma (Español, Inglés, Portugués)
- **Contexto de Conversación**: Mantiene el contexto de la conversación para respuestas más coherentes
- **Manejo Inteligente**: Clasifica mensajes (saludos, preguntas, quejas, soporte técnico)
- **Fácil Integración**: Compatible con Twilio, WhatsApp Business API y webhooks personalizados

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **Groq API**: Modelos de IA rápidos (Llama 3.1)
- **Flask**: Framework web para webhooks
- **Twilio** (Opcional): Integración con WhatsApp Business API
- **python-dotenv**: Gestión de variables de entorno

## 📋 Prerrequisitos

- Python 3.8 o superior
- Cuenta de Groq y API key ([obtener aquí](https://console.groq.com/))
- Acceso a WhatsApp Business API o Twilio (opcional)
- Servidor con acceso a internet

## 🔧 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Jhuomar-Barria/Code-Forge.git
cd Code-Forge/WhatsappBot
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno:**
```bash
cp .env.example .env
```

Edita el archivo `.env` y agrega tu API key de Groq:
```
GROQ_API_KEY=tu_api_key_de_groq_aqui
```

4. **Obtener API Key de Groq:**
   - Visita [Groq Console](https://console.groq.com/)
   - Crea una cuenta o inicia sesión
   - Genera una nueva API key
   - Copia la key al archivo `.env`

## 🚀 Uso

### Método 1: Webhook (Recomendado para producción)

1. **Iniciar el servidor:**
```bash
python whatsapp_bot.py
```

2. **Configurar webhook en tu proveedor de WhatsApp:**
   - Twilio: Configura el webhook URL en el dashboard
   - WhatsApp Business API: Configura el webhook en Meta for Developers
   - URL del webhook: `https://tu-dominio.com/webhook`

### Método 2: Desarrollo Local

Para pruebas locales, puedes usar herramientas como ngrok:

```bash
# Instalar ngrok
# Luego ejecutar:
ngrok http 5000

# Usa la URL de ngrok como webhook
```

### Estructura del Proyecto

```
WhatsappBot/
├── whatsapp_bot.py      # Aplicación principal y servidor Flask
├── groq_client.py       # Cliente para API de Groq
├── message_handler.py   # Procesador de mensajes y generación de respuestas
├── bot_instructions.py  # Instrucciones y prompts del bot
├── config.py           # Configuración y constantes
├── example_usage.py    # Ejemplos de uso del bot
├── requirements.txt     # Dependencias Python
├── start.sh            # Script de inicio rápido
├── .env.example        # Ejemplo de variables de entorno
├── .gitignore         # Archivos ignorados por Git
├── logs/               # Archivos de log
├── sessions/           # Sesiones de WhatsApp
├── README.md           # Documentación principal
└── STRUCTURE.md        # Documentación de estructura
```

## ⚙️ Configuración

### Variables de Entorno Principales

- `GROQ_API_KEY`: Tu API key de Groq (requerido)
- `GROQ_MODEL`: Modelo a usar (default: `llama-3.1-70b-versatile`)
- `GROQ_MAX_TOKENS`: Máximo de tokens por respuesta (default: 500)
- `GROQ_TEMPERATURE`: Creatividad de respuestas 0-1 (default: 0.7)
- `ENABLE_CONTEXT`: Habilitar memoria de conversación (default: true)
- `BOT_LANGUAGE`: Idioma por defecto (es, en, pt)

### Modelos Disponibles en Groq

- `llama-3.1-70b-versatile`: Modelo más potente (recomendado)
- `llama-3.1-8b-instant`: Modelo más rápido
- `mixtral-8x7b-32768`: Alternativa con más contexto

## 🎯 Características del Bot

### Clasificación Inteligente de Mensajes

El bot clasifica automáticamente los mensajes en:
- **Saludos**: Respuestas cálidas y amigables
- **Preguntas**: Respuestas informativas y claras
- **Soporte Técnico**: Instrucciones paso a paso
- **Quejas**: Respuestas empáticas y soluciones
- **Despedidas**: Mensajes cordiales

### Detección de Idioma

El bot detecta automáticamente el idioma del usuario y responde en el mismo idioma, soportando:
- Español
- Inglés
- Portugués

### Contexto de Conversación

Mantiene el contexto de las últimas 10 mensajes para respuestas más coherentes y naturales.

## 📝 Ejemplos de Uso

### Ejemplo 1: Saludo
```
Usuario: Hola
Bot: ¡Hola! 👋 ¿En qué puedo ayudarte hoy?
```

### Ejemplo 2: Pregunta
```
Usuario: ¿Cómo puedo resetear mi contraseña?
Bot: Para resetear tu contraseña, sigue estos pasos:
1. Ve a la página de inicio de sesión
2. Haz clic en "¿Olvidaste tu contraseña?"
3. Ingresa tu email
4. Revisa tu correo para el enlace de restablecimiento
```

### Ejemplo 3: Queja
```
Usuario: El servicio no está funcionando
Bot: Lamento mucho los inconvenientes. Entiendo tu frustración. 
¿Podrías contarme más detalles sobre el problema para poder ayudarte mejor?
```

## 🔐 Seguridad

- Las API keys se almacenan en variables de entorno
- Nunca commitees el archivo `.env` al repositorio
- Usa HTTPS para webhooks en producción
- Implementa rate limiting para prevenir abuso

## 🧪 Testing

```bash
# Probar el bot localmente
python -c "from message_handler import MessageHandler; mh = MessageHandler(); print(mh.process_message('test_user', 'Hola'))"
```

## 📊 Monitoreo

Los logs se guardan en `./logs/bot.log` (configurable en `.env`)

## 🐛 Solución de Problemas

### Error: "GROQ_API_KEY not found"
- Verifica que el archivo `.env` existe y contiene `GROQ_API_KEY`
- Asegúrate de que el archivo está en el directorio raíz del proyecto

### Error: "Rate limit exceeded"
- Groq tiene límites de rate. Considera implementar un sistema de cola
- Reduce `GROQ_MAX_TOKENS` si es necesario

### El bot no responde
- Verifica que el servidor está corriendo
- Revisa los logs en `./logs/bot.log`
- Verifica la conexión a internet

## 📚 Recursos

- [Documentación de Groq](https://console.groq.com/docs)
- [Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)

## 👤 Autor

**Jhuomar Barria**
- Estudiante de Ingeniería de Sistemas y Computación en UTP
- Desarrollador de IA y Backend
- Email: jhuomar3105@gmail.com
- LinkedIn: [Jhuomar Barría](https://www.linkedin.com/in/jhuomar-barría/)

## 📝 Licencia

Este proyecto es parte de un portafolio personal y está disponible para fines educativos.

## 🤝 Contribuciones

Este es un proyecto de portafolio personal. ¡Las sugerencias y feedback son bienvenidos!

## ⚠️ Notas Importantes

- Asegúrate de tener créditos suficientes en tu cuenta de Groq
- La integración de WhatsApp requiere acceso a WhatsApp Business API o Twilio
- Los límites de rate pueden aplicarse según el uso de la API
- Para producción, considera implementar autenticación adicional y rate limiting

---

*Parte del repositorio Code-Forge*

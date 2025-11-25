# Estructura del Proyecto WhatsApp Bot

## 📁 Estructura de Directorios

```
WhatsappBot/
├── whatsapp_bot.py          # Aplicación principal y servidor Flask
├── groq_client.py           # Cliente para API de Groq
├── message_handler.py       # Procesador de mensajes y generación de respuestas
├── bot_instructions.py       # Instrucciones y prompts del bot
├── config.py                # Configuración y constantes
├── example_usage.py         # Ejemplos de uso del bot
├── requirements.txt         # Dependencias Python
├── start.sh                 # Script de inicio rápido
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore              # Archivos ignorados por Git
├── README.md                # Documentación principal
├── STRUCTURE.md             # Este archivo
├── logs/                    # Archivos de log
└── sessions/                # Sesiones de WhatsApp (si aplica)
```

## 📄 Descripción de Archivos

### Archivos Principales

- **whatsapp_bot.py**: Servidor Flask que maneja webhooks de WhatsApp y procesa mensajes
- **groq_client.py**: Cliente para interactuar con la API de Groq
- **message_handler.py**: Lógica para procesar mensajes, clasificarlos y generar respuestas
- **bot_instructions.py**: Prompts y configuraciones del comportamiento del bot
- **config.py**: Configuración centralizada del proyecto

### Archivos de Configuración

- **requirements.txt**: Lista de dependencias Python necesarias
- **.env.example**: Plantilla para variables de entorno
- **.gitignore**: Archivos que no deben ser versionados

### Utilidades

- **example_usage.py**: Ejemplos de cómo usar los componentes del bot
- **start.sh**: Script para iniciar el bot fácilmente

### Directorios

- **logs/**: Almacena archivos de log del bot
- **sessions/**: Almacena sesiones de WhatsApp (si se usa WhatsApp Web)

## 🔧 Mantenimiento

Para mantener la estructura limpia:

1. No agregar archivos temporales o de prueba en la raíz
2. Usar los directorios `logs/` y `sessions/` para archivos generados
3. Mantener los archivos de configuración actualizados
4. Documentar cualquier nuevo archivo o directorio


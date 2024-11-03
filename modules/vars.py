import os

API_ID    = os.environ.get("API_ID", "23159366")
API_HASH  = os.environ.get("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6038363299:AAEQq_ioFG0u0UPBFvsRlEU6NDGB6S-ltQw") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

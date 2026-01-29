import os
from dotenv import load_dotenv

load_dotenv()

# LDAP Configuration
LDAP_URI = os.getenv("LDAP_URI")
LDAP_BIND_DN = os.getenv("LDAP_BIND_DN")
LDAP_PASSWORD = os.getenv("LDAP_PASSWORD")
LDAP_BASE_DN = os.getenv("LDAP_BASE_DN")

# FastAPI Configuration
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))  # Default to 8000 if not set
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

import os
from dotenv import load_dotenv

load_dotenv()

LDAP_URI = os.getenv("LDAP_URI")
LDAP_BIND_DN = os.getenv("LDAP_BIND_DN")
LDAP_PASSWORD = os.getenv("LDAP_PASSWORD")
LDAP_BASE_DN = os.getenv("LDAP_BASE_DN")
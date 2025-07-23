from cryptography.fernet import Fernet
import base64
import hashlib

RAW_KEY = "django-insecure-k56gkbs--)2ud=n$p)8@$z=)#%1o0ez@b=o3tate%a$h*$^90ki8$"

def generate_key(raw_key: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(raw_key.encode()).digest())

FERNET_KEY = generate_key(RAW_KEY)
fernet = Fernet(FERNET_KEY)



def decrypt_message(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
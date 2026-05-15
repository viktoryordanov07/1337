import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

USERS = {
    "admin": hash_password("admin123")
}

def authenticate(username: str, password: str) -> bool:
    return USERS.get(username) == hash_password(password)

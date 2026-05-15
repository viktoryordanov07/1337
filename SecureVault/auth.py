import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

USERS = {
    "Viktor": hash_password("verystrongpassword")
}

def authenticate(username: str, password: str) -> bool:
    return USERS.get(username) == hash_password(password)
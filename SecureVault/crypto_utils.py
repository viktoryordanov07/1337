import base64
import hashlib
from cryptography.fernet import Fernet


def get_cipher(password: str):
    key = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(key)
    return Fernet(key)


def encrypt_file(cipher, data: bytes) -> bytes:
    return cipher.encrypt(data)


def decrypt_file(cipher, data: bytes) -> bytes:
    return cipher.decrypt(data)
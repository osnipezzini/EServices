import os

from cryptography.fernet import Fernet

__all__ = ['encrypt', 'decrypt']


def _get_key():
    return os.environ.get('HASH_KEY').encode('utf8')


def encrypt(message):
    f = Fernet(_get_key())
    encrypted = f.encrypt(message.encode('utf8'))
    return encrypted.decode('utf8')


def decrypt(message):
    f = Fernet(_get_key())
    decrypted = f.decrypt(message.encode('utf8'))
    return decrypted.decode('utf8')

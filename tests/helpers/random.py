import string
from random import choice
from random import randint
from uuid import UUID
from uuid import uuid4


def get_random_int(start: int = 1, stop: int = 1_000_000) -> int:
    return randint(start, stop)

def get_random_string(length=30) -> str:
    return ''.join(choice(string.ascii_lowercase + string.digits) for _ in range(length))

def get_random_bytes(length=30) -> bytes:
    return ''.join(choice(string.ascii_lowercase + string.digits) for _ in range(length)).encode()

def get_random_uuid() -> UUID:
    return uuid4()

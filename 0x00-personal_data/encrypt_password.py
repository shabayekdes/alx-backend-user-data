#!/usr/bin/env python3
"""Password Encryption and Validation Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Generates a salted and hashed password.
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the provided password matches the hashed password.
    """
    valid = False
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        valid = True
    return valid

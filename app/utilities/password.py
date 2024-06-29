import bcrypt


def hash_password(password: str) -> str:
    password = password.encode()
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)

    return hash


def check_password(password: str, hash: bytes) -> str:
    password = password.encode()
    value = bcrypt.checkpw(password, hash)

    if value is not True:
        raise ValueError("Not valid password")

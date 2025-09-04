import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(password.encode(), salt).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

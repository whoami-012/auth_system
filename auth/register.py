import pwinput
from db.database import conn
from utils.security import hash_password


def reg_form():
    username = input("Enter username: ")

    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            print("Username already exists!")
            return

        password = pwinput.pwinput("Enter password: ")
        hashed_password = hash_password(password)

        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
            (username, hashed_password),
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"User '{username}' (id={user_id}) registered successfully")

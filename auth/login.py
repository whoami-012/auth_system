import pwinput, time
from db.database import conn
from utils.security import verify_password


def login_form(max_retries=3, delay=3):
    retries = max_retries

    while retries > 0:
        username = input("Enter Username: ")

        with conn.cursor() as cur:
            cur.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cur.fetchone()

            if not result:
                retries -= 1
                print(f"Username not found! Attempts left: {retries}")
                if retries > 0:
                    time.sleep(delay)
                continue

        password = pwinput.pwinput("Enter Your password: ")

        if verify_password(password, result[0]):
            print("Access granted")
            return True
        else:
            retries -= 1
            print(f"Wrong password. Attempts left: {retries}")
            if retries > 0:
                time.sleep(delay)

    print("Too many failed attempts. Access denied.")
    return False

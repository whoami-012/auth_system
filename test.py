import pwinput, json, os, bcrypt
from pick import pick

def reg_form(username, password):
    if os.path.exists("registration.txt"):
        with open("registration.txt", "r") as infile:
            try:
                registration = json.load(infile)
            except json.JSONDecodeError:
                registration = {}
    else:
        registration = {}

    while True:
        username = input("Enter username: ")
        if username in registration:
            print("username is already taken!")
            continue 
        break
    
    password = input("Enter password: ")
    salt = bcrypt.gensalt(rounds=15)
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    registration[username] = hashed_password.decode()

    with open("registration.txt", "w") as outfile:
        json.dump(registration, outfile)
    print(f"User '{username}' registered successfully ✅")

    return hashed_password

def login_form():
    with open('registration.txt') as f:
        users = json.load(f)

    try:
        username = input("Enter Username: ")
        password = pwinput.pwinput("Enter Your password: ")

        if username in users and bcrypt.checkpw(password.encode(), users[username].encode()):
            print("Access granted.")
        else:
            print("Access denied!")
    except Exception as e:
        print(f"An error occurred: {e}")


def choice():
    title = 'Please choose an option..'
    options = ['register', 'login']
    option, index = pick(options, title, indicator='=>')
    if option == 'register':
        reg_form()
    if option == 'login':
        login_form()

choice()
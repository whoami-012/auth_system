from pick import pick
from db.database import init_db
from auth.register import reg_form
from auth.login import login_form

init_db()


def choice():
    title = "Please choose an option.."
    options = ["register", "login"]
    option, index = pick(options, title, indicator="=>")

    if option == "register":
        reg_form()
    elif option == "login":
        login_form()


if __name__ == "__main__":
    choice()

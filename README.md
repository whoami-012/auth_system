# Python Authentication System

A simple authentication system built with **Python**, **Postgres (Neon DB)**, and **bcrypt**.
Supports secure user registration, login with password hashing, and retry protection.

---

## Features

* User registration with **bcrypt-hashed passwords**
* Login with retry protection (max 3 attempts by default)
* Secure password input using `pwinput`
* Postgres (Neon DB) backend
* Modular project structure (DB, Auth, Utils)

---

## 📂 Project Structure

```
auth_system/
│── main.py              # Entry point (menu system)
│── requirements.txt     # Dependencies
│── .env                 # Environment variables (not committed)
│── db/
│   └── database.py      # Database connection & init
│── auth/
│   ├── register.py      # Registration logic
│   └── login.py         # Login logic
└── utils/
    └── security.py      # Password hashing & verification
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>/<dbname>?sslmode=require
```

### 5. Run the program

```bash
python main.py
```

---

## Security Notes

* Passwords are stored using **bcrypt** (not plaintext ✅).
* `.env` is **ignored by Git** (check `.gitignore`).
* If you deploy this system, use a strong Neon/Postgres password.

---

## 🧩 Future Improvements

* Add Multi-Factor Authentication (MFA) with `pyotp`
* User roles (admin, user, etc.)
* Session management
* API version with FastAPI or Flask

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

---

## License

This project is licensed under the MIT License.

# 🍪 Flask Session Counter App

A simple Flask web application that demonstrates how to use **sessions** to track user visits and manage a counter with multiple increment options.

---

## 🚀 Features

- Track number of visits per user session
- Increment counter by:
  - ➕ +1
  - ✖️ +2
  - 🔢 Custom value (user input)

- 🔄 Reset counter
- 🧹 Destroy session (clear all data)

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML (Jinja Templates)

---

## 📂 Project Structure

```
dojo_fruit_store/
│
├── static/          # CSS / JS (if any)
├── templates/
│   └── index.html   # Main UI
├── server.py        # Flask app
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone <your-repo-link>
cd dojo_fruit_store
```

2. Create virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install flask
```

4. Run the app:

```bash
python server.py
```

5. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

- Uses Flask **session** to store:
  - `visits` → number of times user accessed the page
  - `counter` → current counter value

### Routes:

| Route               | Method | Description              |
| ------------------- | ------ | ------------------------ |
| `/`                 | GET    | Display visits & counter |
| `/increment`        | GET    | +1 counter               |
| `/double`           | GET    | +2 counter               |
| `/increment_custom` | POST   | Add custom value         |
| `/reset`            | GET    | Reset counter to 0       |
| `/destroy_session`  | GET    | Clear all session data   |

---

## 🔐 Session Security Note

This app uses:

```python
app.secret_key = "12345678"
```

⚠️ In production:

- Use a strong, random secret key
- Keep it private and secure

---

## 🍪 Cookie Debugging (Advanced)

To decode Flask session cookies:

1. Install tool:

```bash
pip install flask-unsign
```

2. Copy cookie value from browser:

- Open DevTools → Application → Cookies

3. Decode:

```bash
flask-unsign --decode --cookie "your_cookie_value"
```

---

## 💡 Learning Goals

- Understand Flask sessions
- Handle user state without database
- Work with routes and forms
- Practice redirect flow

---

## 📌 Future Improvements

- Add database (SQLite / MySQL)
- Add user authentication
- Improve UI with Bootstrap
- Add persistent counters

---

## 👨‍💻 Author

Shams – Full Stack Developer (Flask + Frontend)

---

## ⭐ If you like this project

Give it a star on GitHub ⭐

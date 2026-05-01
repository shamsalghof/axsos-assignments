# 👥 Users Table - Flask Project

## 📌 Overview

This is a simple Flask web application that displays a list of users in a clean HTML table using **Bootstrap** for styling.

The project demonstrates:

* Passing data from Python (Flask) to HTML (Jinja2)
* Looping through data in templates
* Rendering dynamic content

---

## 🚀 Features

* Display users in a table
* Show:

  * First Name
  * Last Name
  * Full Name (combined)
* Clean UI using Bootstrap
* Simple and beginner-friendly structure

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌶️
* HTML5
* Bootstrap 5
* Jinja2 (templating engine)

---

## 📂 Project Structure

```
project_folder/
│
├── server.py
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1. Clone or download the project

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

```bash
.venv\Scripts\activate   # Windows
```

### 4. Install dependencies

```bash
pip install flask
```

---

## ▶️ Run the App

```bash
python server.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/users
```

---

## 🧠 How It Works

### 🔹 Backend (Flask)

* Defines a route `/users`
* Creates a list of users (Python dictionaries)
* Sends data to HTML using `render_template`

```python
@app.route('/users')
def render_lists():
    users_list = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    return render_template('index.html', users=users_list)
```

---

### 🔹 Frontend (HTML + Jinja)

* Loops through users using Jinja
* Displays data dynamically in a table

```html
{% for user in users %}
<tr>
  <td>{{ user.first_name }}</td>
  <td>{{ user.last_name }}</td>
  <td>{{ user.first_name }} {{ user.last_name }}</td>
</tr>
{% endfor %}
```

---

## 🎨 UI

* Uses Bootstrap classes:

  * `table`
  * `table-bordered`
  * `table-striped`
  * `table-hover`

---

## 💡 Future Improvements

* ➕ Add user form (POST request)
* 🔍 Search/filter users
* 🗑️ Delete user
* ✏️ Edit user
* 🗄️ Connect to database (SQLite / MySQL)

---

## 👩‍💻 Author

Shams – UX/UI Designer → Full Stack Developer 🚀

---

## 📄 License

This project is open-source and free to use.

# 🎨 Flask Checkerboard Project

## 📌 Overview

This project is a simple web application built using Flask that generates a dynamic checkerboard pattern.

Users can customize:

- Number of rows
- Number of columns
- Colors of the board

---

## 🚀 Features

- Default 8x8 checkerboard
- Dynamic row control
- Custom grid size
- Full customization (size + colors)

---

## 🧠 Technologies Used

- Python
- Flask
- HTML (Jinja Templates)
- CSS

---

## 📂 Project Structure

```
project/
│
├── server.py
├── templates/
│   └── index.html
└── static/
    └── style.css (optional)
```

---

## ▶️ How to Run

1. Install Flask:

```
pip install flask
```

2. Run the server:

```
python server.py
```

3. Open browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Routes

### 1. Default Board

```
/
```

➡️ Displays 8x8 board

---

### 2. Custom Rows

```
/<number>
Example: /5
```

➡️ 5 rows, 8 columns

### 3. Custom Size

```
/<rows>/<columns>
Example: /5/10
```

➡️ 5 rows, 10 columns

---

### 4. Full Customization

```
/<rows>/<columns>/<color1>/<color2>
Example: /5/10/blue/yellow
```

➡️ Fully customized board

---

## 🎯 Example URLs

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/6
- http://127.0.0.1:5000/6/12
- http://127.0.0.1:5000/6/12/green/black

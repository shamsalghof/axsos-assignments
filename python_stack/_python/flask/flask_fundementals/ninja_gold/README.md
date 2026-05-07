# Ninja Gold Game

A simple Flask web application where a ninja earns or loses gold by visiting different locations such as farms, caves, houses, and casinos.

---

## Features

- Start with **0 gold**
- Earn gold from:
  - Farm → 10–20 gold
  - Cave → 5–10 gold
  - House → 2–5 gold
- Casino can:
  - Win up to 50 gold
  - Lose up to 50 gold
- Track all activities with timestamps
- Display activity history in different colors:
  - Green for earnings
  - Red for losses

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2
- Sessions

---

## Project Structure

```bash
ninja_gold/
│
├── server.py
│
├── templates/
│   └── index.html
│
└── static/
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd ninja_gold
```

### 3. Install Flask

```bash
pip install flask
```

---

## Run the Application

```bash
python server.py
```

Open your browser and visit:

```bash
http://localhost:5000
```

---

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Displays the main game page |
| `/process_money` | POST | Processes gold earnings/losses |

---

## How the Game Works

Each building sends a hidden value through a form:

```html
<input type="hidden" name="building" value="farm">
```

The Flask server receives the building name and randomly generates gold based on the selected location.

Example:

```python
if building == "farm":
    gold = random.randint(10, 20)
```

The total gold and activities are stored using Flask sessions.

---

## Example Activity Log

```text
Earned 15 gold from the farm! (2026/05/07 04:15 PM)

Entered a casino and lost 30 gold... Ouch. (2026/05/07 04:20 PM)
```

---

## Learning Objectives

- Flask routing
- Handling POST requests
- Using sessions
- Working with forms
- Using random values in Python
- Rendering dynamic data with Jinja2

---

## Author

Shams
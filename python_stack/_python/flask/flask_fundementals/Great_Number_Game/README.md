# Great Number Game 🎯

A simple Flask web application where the player tries to guess a random number between **1 and 100** within **5 attempts**.

## Features
- Random number generation
- User guesses handled with Flask forms
- Session storage for game state
- Tracks number of attempts
- Displays:
  - Too High
  - Too Low
  - Correct Guess
  - Game Over
- Automatically restarts after game ends

---

## Technologies Used
- Python
- Flask
- HTML/CSS
- Sessions

---

## Project Structure

```bash
great_number_game/
│
├── server.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
```

### 2. Navigate to the project folder

```bash
cd great_number_game
```

### 3. Create virtual environment

```bash
python -m venv FlaskEnv
```

### 4. Activate virtual environment

#### Windows

```bash
FlaskEnv\Scripts\activate
```

#### Mac/Linux

```bash
source FlaskEnv/bin/activate
```

### 5. Install Flask

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
http://127.0.0.1:5000
```

---

## How to Play

1. The app generates a random number between 1 and 100.
2. Enter your guess.
3. You have only 5 attempts.
4. The game will tell you if your guess is:
   - Too high
   - Too low
   - Correct
5. If you fail after 5 attempts, you lose.

---

## Main Flask Routes

### `/`
Displays the game page.

### `/guess`
Handles the user's guess and updates the game state.

---

## Example Game Logic

```python
if user_guess > number:
    session['result'] = "high"
elif user_guess < number:
    session['result'] = "low"
else:
    session['result'] = "correct"
```

---

## Author

Created by Shams 🚀
# Great Number Game

## Assignment: Great Number Game

### Objectives

- Practice using Django Sessions to store data about a client's history with the web application.
- Practice clearing session data.
- Practice handling user-submitted form data.
- Build a number guessing game using Django.

---

## Description

The Great Number Game is a simple web application where the server generates a random number between **1 and 100** and stores it in the user's session.

The player attempts to guess the number. After each guess, the application responds with one of the following:

- Too High
- Too Low
- Correct

The game continues until the correct number is guessed.

---

## Features

### Required Features

#### Home Page (`/`)

- Generates a random number between 1 and 100.
- Stores the number in session.
- Displays a form where the user can submit a guess.

#### Guess Route

- Accepts the user's guess.
- Compares it with the session number.
- Displays whether the guess is:
  - Too High
  - Too Low
  - Correct

#### Play Again

- Clears the current game session.
- Generates a new random number.
- Starts a new game.

---

## Random Number Generation

```python
import random

random.randint(1, 100)
```

This generates a random integer between 1 and 100.

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd great_number_game
```

### Create a Virtual Environment

```bash
python -m venv env
```

#### Windows

```bash
env\Scripts\activate
```

#### macOS / Linux

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py migrate
```

### Start the Server

```bash
python manage.py runserver
```

Open:

```text
http://localhost:8000
```

---

## Routes

| Route | Description |
|---------|-------------|
| `/` | Displays the game page |
| `/guess` | Processes the user's guess |
| `/reset` | Starts a new game |

---

## Example Gameplay

### Initial Screen

```text
I'm thinking of a number between 1 and 100.

Take a guess!

[ Enter Number ]
[ Guess ]
```

### Too Low

```text
25

Too Low!
```

### Too High

```text
88

Too High!
```

### Correct

```text
42

42 was the number!

Play Again?
```

---

## Ninja Bonus Features

### Styled Results

Display results using different colors:

| Result | Color |
|----------|--------|
| Too High | Red |
| Too Low | Red |
| Correct | Green |

### Unlimited Guesses

Allow the user to continue guessing until the correct number is found.

### Attempt Counter

Track and display the number of guesses made.

Example:

```text
Correct!

You guessed the number in 6 attempts.
```

---

## Sensei Bonus Features

### Maximum 5 Attempts

Limit the player to 5 guesses.

If the player fails to guess correctly:

```text
You Lose!

The correct number was 42.
```

Provide a button to start a new game.

### Leaderboard

When a player wins:

1. Prompt for their name.
2. Save:
   - Name
   - Number of attempts

Display all winners on a leaderboard page.

Example:

| Rank | Name | Attempts |
|------|------|----------|
| 1 | Sarah | 2 |
| 2 | John | 3 |
| 3 | Alex | 5 |

Additional route:

| Route | Description |
|---------|-------------|
| `/leaderboard` | Displays all winners and scores |

---

## Session Variables Example

```python
request.session['random_number']
request.session['attempts']
request.session['result']
```

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- Django Templates
- Django Sessions

---

## Learning Outcomes

By completing this assignment, you will learn how to:

- Create and manage sessions in Django.
- Store game state between requests.
- Process form submissions.
- Use conditional rendering in templates.
- Build interactive web applications.
- Track user progress and statistics.

---

## Author

Created as part of the Django Sessions curriculum assignment.
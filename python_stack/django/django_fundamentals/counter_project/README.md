# Counter App

## Assignment: Counter

### Objectives

* Practice using **Django Sessions** to store data about a specific client's history with the application.
* Learn how to check whether a session exists.
* Learn how to initialize a session.
* Learn how to modify session data.
* Build a Django application that counts the number of times the root route (`/`) has been viewed.

---

## Description

This project demonstrates the use of Django sessions by tracking how many times a user has visited the website.

Each time the user visits the home page, the visit count is stored and updated in the session. The application also provides a way to clear the session and reset the counter.

---

## Features

### Required Features

#### Home Page (`/`)

* Displays the number of times the client has visited the site.
* Refreshing the page increments the visit count.

#### Destroy Session (`/destroy_session`)

* Clears the session data.
* Redirects the user back to the home page.
* Counter starts over after the session is destroyed.

---

## Session Tips

### Check if a Session Key Exists

```python
if 'key_name' in request.session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")
```

### Delete a Specific Session Key

```python
del request.session['key_name']
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd counter
```

### 2. Create and Activate a Virtual Environment

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

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Visit:

```text
http://localhost:8000
```

---

## Routes

| Route              | Description                               |
| ------------------ | ----------------------------------------- |
| `/`                | Displays and increments the visit counter |
| `/destroy_session` | Clears the session and resets the counter |

---

## Ninja Bonus

### Reset Button

Add a button on the homepage that sends the user to:

```text
/destroy_session
```

to reset the counter.

### +2 Button

Add:

* A button labeled **+2**
* A route that increments the counter by 2 instead of 1

Example:

```text
/increment_by_two
```

---

## Sensei Bonus

### Custom Increment Form

Allow the user to enter a custom increment value.

Example:

```html
<form action="/increment" method="post">
    {% csrf_token %}
    <input type="number" name="increment">
    <button type="submit">Add</button>
</form>
```

The counter should increase based on the value submitted by the user.

### Display Visits and Counter Separately

Track and display:

* Number of page visits
* Current counter value

Example:

```text
You have visited this page 10 times.

Counter Value: 25
```

---

## Example Output

```text
Counter

You have visited this page 5 times.

Current Counter Value: 5

[+2] [Reset]
```

---

## Technologies Used

* Python
* Django
* HTML
* Django Templates
* Django Sessions

---

## Author

Created as part of the Django Sessions assignment.

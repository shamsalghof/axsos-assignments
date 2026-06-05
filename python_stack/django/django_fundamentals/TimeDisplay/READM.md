# ⏰ Time Display — Django Assignment

A simple Django project that displays the current date and time on the homepage.

---

## 🎯 Objectives

- Practice setting up a Django project
- Pass data from a view to a template
- Connect and use custom static files (CSS)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd time_display
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Now visit [http://localhost:8000](http://localhost:8000) or [http://localhost:8000/time_display](http://localhost:8000/time_display) in your browser.

---

## 📁 Project Structure

```
time_display_project/
├── manage.py
├── time_display_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── time_display/
    ├── static/
    │   └── time_display/
    │       └── style.css
    ├── templates/
    │   └── index.html
    ├── views.py
    └── urls.py
```

---

## 🧠 How It Works

### `views.py`

The view retrieves the current time and passes it to the template via context:

```python
from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
```

### `index.html`

The template displays the time using Django's template syntax:

```html
<h1>Current Time</h1>
<p>{{ time }}</p>
```

### Static Files

Custom CSS is linked using Django's `{% static %}` tag:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'time_display/style.css' %}">
```

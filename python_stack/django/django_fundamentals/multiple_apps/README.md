# Multiple Apps

## Assignment: Multiple Apps

### Objectives

- Practice creating multiple Django apps.
- Learn how to organize a Django project using multiple apps.
- Practice using `include()` to route requests to different applications.
- Understand how reusable Django apps can be shared across projects.

---

## Description

In this assignment, you will expand your existing Django project by adding multiple applications.

The project will contain three separate apps:

- Blogs
- Surveys
- Users

Each app will manage its own URLs and views while being connected through the main project URL configuration.

This structure demonstrates one of Django's greatest strengths: building reusable applications that can be plugged into multiple projects.

---

## Project Structure

```text
multiple_apps_project/
│
├── blogs/
├── surveys/
├── users/
│
├── multiple_apps_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── manage.py
```

---

## Main Project URLs

The main `urls.py` should delegate routes to the appropriate app.

```python
from django.urls import path, include

urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('surveys/', include('surveys.urls')),
    path('', include('users.urls')),
]
```

---

# Blogs App

## Routes

### `/blogs`

Display:

```text
placeholder to display a list of all blogs
```

Method:

```python
index
```

---

### `/blogs/new`

Display:

```text
placeholder to display a new form to create a new blog
```

Method:

```python
new
```

---

### `/blogs/create`

Redirect to:

```text
/blogs
```

Method:

```python
create
```

---

### `/blogs/<number>`

Display:

```text
placeholder to display blog number: <number>
```

Method:

```python
show
```

Example:

```text
/blogs/5

placeholder to display blog number: 5
```

---

### `/blogs/<number>/edit`

Display:

```text
placeholder to edit blog <number>
```

Method:

```python
edit
```

Example:

```text
/blogs/5/edit

placeholder to edit blog 5
```

---

### `/blogs/<number>/delete`

Redirect to:

```text
/blogs
```

Method:

```python
destroy
```

---

# Surveys App

## Routes

### `/surveys`

Display:

```text
placeholder to display all the surveys created
```

Method:

```python
index
```

---

### `/surveys/new`

Display:

```text
placeholder for users to add a new survey
```

Method:

```python
new
```

---

# Users App

## Routes

### `/register`

Display:

```text
placeholder for users to create a new user record
```

Method:

```python
register
```

---

### `/login`

Display:

```text
placeholder for users to log in
```

Method:

```python
login
```

---

### `/users/new`

Should use the same method as:

```text
/register
```

Method:

```python
register
```

---

### `/users`

Display:

```text
placeholder to display all the list of users later
```

Method:

```python
users
```

---

## Example URLs Configuration

### blogs/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
]
```

---

### surveys/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
]
```

---

### users/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.users),
]
```

---

## Required Features Checklist

- [ ] Create a Blogs app.
- [ ] Create a Surveys app.
- [ ] Create a Users app.
- [ ] Configure app URLs using `include()`.
- [ ] Complete `/blogs`.
- [ ] Complete `/blogs/new`.
- [ ] Complete `/blogs/create`.
- [ ] Complete `/blogs/<number>`.
- [ ] Complete `/blogs/<number>/edit`.
- [ ] Complete `/blogs/<number>/delete`.
- [ ] Complete `/surveys`.
- [ ] Complete `/surveys/new`.
- [ ] Complete `/register`.
- [ ] Complete `/login`.
- [ ] Complete `/users/new`.
- [ ] Complete `/users`.

---

## Ninja Bonus

Use the same view method for:

```text
/
```

and

```text
/blogs
```

Example:

```python
path('', views.index)
path('blogs/', views.index)
```

Both routes should display:

```text
placeholder to display a list of all blogs
```

---

## Technologies Used

- Python
- Django
- URL Routing
- Django Apps
- Django Views

---

## Learning Outcomes

By completing this assignment, you will learn how to:

- Create multiple Django apps in a single project.
- Organize large Django projects.
- Use URL routing with `include()`.
- Reuse applications across projects.
- Build modular and maintainable Django applications.

---

## Author

Created as part of the Django Fundamentals curriculum.
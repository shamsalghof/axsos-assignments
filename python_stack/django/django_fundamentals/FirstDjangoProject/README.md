# First Django Project

## Overview

This project is a simple Django application created to practice:

* Setting up a Django project
* Creating a Django app
* Configuring URL routes
* Creating view functions
* Returning HTTP responses
* Using route parameters
* Returning JSON responses

---

## Objectives

* Practice setting up a new Django project
* Practice setting up a new Django app
* Learn Django routing
* Learn how views return responses
* Use route parameters in URLs
* Return JSON data using `JsonResponse`

---

## Routes Implemented

| Route                    | Method    | Description                                            |
| ------------------------ | --------- | ------------------------------------------------------ |
| `/`                      | `root`    | Redirects to `/blogs`                                  |
| `/blogs`                 | `index`   | Displays a placeholder message for all blogs           |
| `/blogs/new`             | `new`     | Displays a placeholder message for creating a new blog |
| `/blogs/create`          | `create`  | Redirects to `/`                                       |
| `/blogs/<number>`        | `show`    | Displays the selected blog number                      |
| `/blogs/<number>/edit`   | `edit`    | Displays a placeholder message for editing a blog      |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs`                                  |
| `/blogs/json`            | `json`    | Returns JSON data                                      |

---

## Example Responses

### GET `/blogs`

```text
placeholder to later display a list of all blogs
```

### GET `/blogs/new`

```text
placeholder to display a new form to create a new blog
```

### GET `/blogs/15`

```text
placeholder to display blog number: 15
```

### GET `/blogs/15/edit`

```text
placeholder to display blog number: 15 edit
```

### GET `/blogs/json`

```json
{
  "title": "Shams Alghof",
  "skills": [
    "HTML",
    "CSS",
    "JS",
    "Python",
    "Flask",
    "Django"
  ]
}
```

---

## Technologies Used

* Python 3
* Django 5

---

## Running the Project

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd FirstDjangoProject
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

or on Windows:

```bash
venv\Scripts\activate
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Author

**Shams Alghof**

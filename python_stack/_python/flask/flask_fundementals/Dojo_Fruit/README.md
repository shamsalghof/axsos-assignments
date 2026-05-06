🍓 Dojo Fruit Store (Flask Project)
📌 Overview
This is a simple web application built using Python and Flask that simulates a fruit store checkout system.
Users can select quantities of fruits, submit their order, and view a checkout summary.

🚀 Features
Display fruit selection page

Handle form submission using POST request

Calculate total number of fruits

Show customer information (name, student ID)

Display checkout summary with timestamp

🛠️ Technologies Used
Python 3

Flask (Web Framework)

HTML (Jinja Templates)

Bootstrap (optional for styling)

📂 Project Structure
project/
│
├── server.py
├── templates/
│   ├── index.html
│   ├── fruits.html
│   └── checkout.html
└── README.md
▶️ How to Run
Create a virtual environment (optional but recommended):

python -m venv flaskEnv
Activate the environment:

flaskEnv\Scripts\activate   # Windows
source flaskEnv/bin/activate  # Mac/Linux
Install Flask:

pip install flask
Run the server:

python server.py
Open your browser:

http://localhost:5000
🔄 Routes
/
Displays the homepage (index.html)

/fruits
Displays fruit selection page

/checkout (POST)
Handles form submission

Retrieves:

Strawberry, Raspberry, Apple quantities

First name, Last name, Student ID

Calculates total fruits

Passes data to checkout.html

/checkout/result
Displays checkout result page

🧠 Key Concepts Used
Flask routing (@app.route)

Handling form data with request.form

Using Jinja templates (render_template)

Passing variables from backend to frontend

Basic data processing in Python

🧾 Example Output
After submitting the form:

User sees total fruits ordered

Their name and student ID

Current date and time of checkout

⚠️ Notes
All form values are received as strings → converted to integers when needed

Default values are used to prevent errors if inputs are missing

Debug mode is enabled for development

📈 Future Improvements
Add prices and calculate total cost 💰

Store orders in a database 🗄️

Add validation for inputs ✅

Improve UI/UX design 🎨

Add authentication (login system) 🔐


from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []

    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():

    building = request.form['building']
    gold = 0

    if building == "farm":
        gold = random.randint(10, 20)

    elif building == "cave":
        gold = random.randint(5, 10)

    elif building == "house":
        gold = random.randint(2, 5)

    elif building == "casino":
        gold = random.randint(-50, 50)

    session['gold'] += gold

    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if gold >= 0:
        message = f"Earned {gold} gold from the {building}! ({time})"
    else:
        message = f"Entered a casino and lost {abs(gold)} gold... Ouch. ({time})"

    session['activities'].insert(0, message)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
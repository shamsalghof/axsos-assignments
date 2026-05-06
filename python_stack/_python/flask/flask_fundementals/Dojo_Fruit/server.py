from flask import Flask, render_template, request, redirect
import datetime

# Create Flask app instance
app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template("index.html")


# Checkout route (POST method only)
@app.route('/checkout', methods=['POST'])
def checkout():

    # Get form data from HTML form
    strawberry = request.form.get('strawberry', 0)
    raspberry  = request.form.get('raspberry', 0)
    apple      = request.form.get('apple', 0)

    # Get user info from form
    fname = request.form.get('first_name', '')
    lname = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')

    # Calculate total fruits (convert strings → int)
    total = int(strawberry) + int(raspberry) + int(apple)

    # Get current date and time
    now = datetime.datetime.now()

    # Send data to checkout.html template
    return render_template(
        "checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        apple=apple,
        fname=fname,
        lname=lname,
        student_id=student_id,
        total=total,
        now=now
    )


# Checkout result page (GET method)
@app.route('/checkout/result')
def checkout_result():
    return render_template("checkout.html")


# Fruits page route
@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


# Run the app in debug mode (development only)
if __name__ == "__main__":
    app.run(debug=True)
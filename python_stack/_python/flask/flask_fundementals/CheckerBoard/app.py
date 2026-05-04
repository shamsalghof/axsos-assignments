from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# ----------------------------------------
# Route 1: Default route
# URL: /
# Description:
# Displays an 8x8 grid with default colors (red & black)
# ----------------------------------------
@app.route('/')
def index():
    return render_template("index.html", x=8, y=8, color1="red", color2="black")


# ----------------------------------------
# Route 2: Dynamic rows
# URL: /<x>
# Example: /5
# Description:
# Displays x rows and 8 columns
# ----------------------------------------
@app.route('/<int:x>')
def row_count(x):
    return render_template("index.html", x=x, y=8, color1="red", color2="black")


# ----------------------------------------
# Route 3: Custom grid size
# URL: /<x>/<y>
# Example: /5/10
# Description:
# Displays grid with x rows and y columns
# ----------------------------------------
@app.route('/<int:x>/<int:y>')
def custom_size(x, y):
    return render_template("index.html", x=x, y=y, color1="red", color2="black")


# ----------------------------------------
# Route 4: Full customization
# URL: /<x>/<y>/<color1>/<color2>
# Example: /5/10/blue/yellow
# Description:
# Customize rows, columns, and colors
# ----------------------------------------
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def full_custom(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True)
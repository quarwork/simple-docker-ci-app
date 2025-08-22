# Import the Flask framework to create the web application
from flask import Flask

# Import the random module to generate random numbers
import random

# Create a Flask application instance
# "__name__" tells Flask where to look for resources like templates and static files
app = Flask(__name__)

# Define a route for the root URL ("/")
# When a user visits the homepage, this function will be executed
@app.route("/")
def home():
    # Generate a random color in HEX format (e.g., #7ae634)
    # "%06x" ensures the color code is always 6 hexadecimal digits
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    
    # Return a simple HTML response
    # The text "Random Color: ..." will be displayed in the generated color
    return f"<h1 style='color:{color}'>Random Color: {color}</h1>"

# Run the app only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server
    # host="0.0.0.0" makes the app accessible from outside the container
    # port=5000 is the default port for Flask apps
    app.run(host="0.0.0.0", port=5000)

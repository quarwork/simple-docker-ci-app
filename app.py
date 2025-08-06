from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    return f"<h1 style='color:{color}'>Random Color: {color}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
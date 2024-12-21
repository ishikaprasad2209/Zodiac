from flask import Flask, render_template, request
from logic import get_zodiac_sign
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/zodiac", methods=["POST"])
def zodiac():
    dob_str = request.form["dob"]
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    zodiac_sign = get_zodiac_sign(dob)
    return f"""
    <div style='font-size: 2em; text-align: center; margin-top: 20%; font-family: Arial, sans-serif;'>
        Your Zodiac Sign is: <strong>{zodiac_sign}</strong>
        <br><a href="/" style="text-decoration: none; color: #0078d7;">Go Back</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import random

app = Flask(__name__)

compliments = {
    "happy": [
        "You light up the room!",
        "Your energy is amazing!",
        "You make good vibes look easy!"
    ],
    "sad": [
        "You are stronger than you think.",
        "Even on hard days, you matter a lot.",
        "You’ve got this — one step at a time."
    ],
    "tired": [
        "You’ve already done more than enough today.",
        "Rest is productive too.",
        "You’re doing better than you think."
    ],
    "excited": [
        "Your enthusiasm is contagious!",
        "Big things suit you.",
        "You bring spark to everything!"
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compliment", methods=["POST"])
def compliment():
    name = request.form.get("name")
    mood = request.form.get("mood")

    if mood in compliments:
        message = random.choice(compliments[mood])
    else:
        message = "You are awesome just as you are!"

    return render_template("result.html", name=name, mood=mood, message=message)

if __name__ == "__main__":
    app.run(debug=True)
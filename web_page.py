from flask import Flask, render_template, request
from twitter_friends import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        username = request.form['username']
        friends = get_friends(username)
        draw_map(friends)
    return render_template("Friends_map.html")


if __name__ == "__main__":
    app.run(debug=True)

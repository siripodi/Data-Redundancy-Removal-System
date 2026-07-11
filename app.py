from flask import Flask, render_template, request
from firebase_config import db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        users = db.collection("users")

        docs = users.where("email", "==", email).stream()

        duplicate = False

        for doc in docs:
            duplicate = True

        if duplicate:
            message = "❌ Duplicate Data Found!"

        else:
            users.add({
                "name": name,
                "email": email
            })

            message = "✅ Data Added Successfully!"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])

        prediction = model.predict([[study_hours, attendance, previous_marks]])

        result = prediction[0]

        if result >= 75:
            category = "Good"
        elif result >= 50:
            category = "Average"
        else:
            category = "Poor"

        return render_template("index.html",
                               prediction=round(result, 2),
                               category=category)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
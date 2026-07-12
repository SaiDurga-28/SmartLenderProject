from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction")
def prediction():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["Gender"]),
        float(request.form["Married"]),
        float(request.form["Dependents"]),
        float(request.form["Education"]),
        float(request.form["Self_Employed"]),
        float(request.form["ApplicantIncome"]),
        float(request.form["CoapplicantIncome"]),
        float(request.form["LoanAmount"]),
        float(request.form["Loan_Amount_Term"]),
        float(request.form["Credit_History"]),
        float(request.form["Property_Area"])
    ]

    feature_names = [
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area"
    ]

    features_df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(features_df)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Not Approved"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
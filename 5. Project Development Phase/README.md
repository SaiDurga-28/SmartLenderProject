# Smart Lender - AI Powered Loan Approval Prediction

## Project Overview

Smart Lender is a Machine Learning based web application that predicts whether a loan application is likely to be approved based on the applicant's information. The application helps automate the loan approval process by analyzing applicant details using a trained Machine Learning model.

---

## Objective

The objective of this project is to predict loan approval status using applicant information such as:

- Gender
- Marital Status
- Number of Dependents
- Education
- Self Employment
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

The system predicts whether the loan will be:

- ✅ Loan Approved
- ❌ Loan Not Approved

---

## Features

- Modern and Responsive User Interface
- AI Powered Loan Prediction
- Machine Learning Based Decision Making
- Flask Web Application
- Real-time Loan Prediction
- Easy-to-use Form Interface
- Responsive Design for Desktop and Mobile

---

## Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Pickle

### Web Technologies
- Flask
- HTML5
- CSS3

### Development Tools
- VS Code
- Jupyter Notebook
- Git & GitHub

---

## Project Structure

```
SmartLenderProject/

├── Dataset/
│   └── loan_prediction.csv
│
├── Notebook/
│   └── SmartLender.ipynb
│
├── Flask/
│   ├── app.py
│   ├── model.pkl
│   ├── templates/
│   │   ├── home.html
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
│
├── Screenshots/
│   ├── 01_Home_Page.png
│   ├── 02_Prediction_Form.png
│   ├── 03_Loan_Approved.png
│   └── 04_Loan_Not_Approved.png
│
├── requirements.txt
└── README.md
```

---

## Machine Learning Workflow

- Data Collection
- Data Cleaning
- Handling Missing Values
- Exploratory Data Analysis (EDA)
- Data Visualization
- Label Encoding
- Train-Test Split
- Model Training
- Model Evaluation
- Model Deployment using Flask

---

## Machine Learning Model

**Algorithm Used:**

- Random Forest Classifier

**Model Accuracy:**

- **78.86%**

**Problem Type**

- Binary Classification

---

## Requirements

- Python 3.11+
- Flask
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
---

## How to Run the Project

### Step 1

Clone the repository

```bash
git clone <repository-link>
```

### Step 2

Navigate to the Flask folder

```bash
cd Flask
```

### Step 3

Install dependencies

```bash
pip install flask numpy pandas scikit-learn matplotlib seaborn
```

### Step 4

Run the application

```bash
python app.py
```

### Step 5

Open your browser

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. Open the application.
2. Click **Get Started**.
3. Enter applicant details.
4. Click **Predict Loan**.
5. View the prediction result.

---

## Demo Video

Watch a short demonstration of the **Smart Lender – AI Powered Loan Approval Prediction** project, showcasing the application's features and loan prediction workflow.

**Demo Video:**  
https://drive.google.com/file/d/1FeoKdbpCWkuW60Nmh-MVOuQHtHU0pr9k/view?usp=sharing

---

## Future Scope

- Improve prediction accuracy using advanced ensemble models.
- Deploy the application on a cloud platform.
- Add user authentication and loan history tracking.
- Integrate with banking databases and APIs.
- Provide downloadable loan prediction reports.

---

## Conclusion

The Smart Lender application demonstrates how Machine Learning can be integrated with a Flask web application to automate loan approval prediction. The project combines data preprocessing, model training, and web deployment to provide a simple and interactive prediction system.
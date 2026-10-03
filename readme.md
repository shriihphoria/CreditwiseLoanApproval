<div align="center">

# CreditWiseLoan — Loan Approval Prediction

### End-to-End Machine Learning Project with Streamlit

[![Open Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://creditwiseloanapproval-7xznu2eursfhfzrswihvqc.streamlit.app/)

</div>

---

## 🚀 Live Demo

**[Try CreditWiseLoan →](https://creditwiseloanapproval-7xznu2eursfhfzrswihvqc.streamlit.app/)**

An interactive Streamlit application that predicts loan approval based on applicant and financial information.

---

## 📌 Overview

**CreditWiseLoan** is a machine learning classification project that predicts whether a loan application will be **approved or rejected**.

The project covers the complete ML workflow:

**Data Analysis → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment**

The final **Logistic Regression** model is integrated into a Streamlit web application for real-time predictions.

---

## 🎯 Problem Statement

Loan approval can depend on factors such as:

- Applicant & Coapplicant Income
- Credit Score
- Existing Loans
- DTI Ratio
- Savings
- Collateral Value
- Loan Amount
- Employment Status
- Education
- Property Area
- Loan Purpose

The target variable is:

| Value | Meaning |
|---:|---|
| `0` | Rejected |
| `1` | Approved |

```text
Loan_Approved
```

---

## 📊 Dataset

The dataset contains **1,000 loan application records** with **19 original features**.

### Main Features

| Category | Features |
|---|---|
| Financial | Income, Savings, DTI Ratio, Loan Amount, Collateral |
| Credit | Credit Score, Existing Loans |
| Personal | Age, Gender, Marital Status, Dependents |
| Employment | Employment Status, Employer Category |
| Loan | Loan Term, Loan Purpose |
| Property | Property Area |
| Education | Education Level |

### Feature Engineering

Two additional features were created:

```text
Credit_Score_sq
DTI_Ratio_sq
```

The final model uses **27 features** after encoding and feature engineering.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
EDA & Data Cleaning
   ↓
Missing Value Handling
   ↓
Encoding & Feature Engineering
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Logistic Regression Selection
   ↓
Streamlit Deployment
```

---

## 🤖 Models & Performance

Three classification models were evaluated:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 87.50% | 87.56% | 87.50% | 87.53% |
| KNN | 80.00% | 79.45% | 80.00% | 78.71% |
| Gaussian Naive Bayes | 86.50% | 86.44% | 86.50% | 86.47% |

### Deployed Model

**Logistic Regression**

The trained model is stored in:

```text
model.pkl
```

The preprocessing components are stored in:

```text
preprocessing.pkl
```

---

## 🧪 Application Testing

The deployed application was tested using five different applicant profiles.

| Test Case | Prediction | Probability |
|---:|---|---:|
| 1 | ✅ Approved | 91.86% |
| 2 | ❌ Rejected | 0.00% |
| 3 | ✅ Approved | 99.92% |
| 4 | ❌ Rejected | 0.36% |
| 5 | ❌ Rejected | 0.00% |

> **Note:** Model probabilities represent predictions based on patterns learned from the training dataset and should not be interpreted as real-world loan approval probabilities.

---

## 🌐 Streamlit Application

Users can enter:

- Applicant income
- Coapplicant income
- Age
- Dependents
- Credit score
- Existing loans
- DTI ratio
- Savings
- Collateral value
- Loan amount
- Loan term
- Education
- Gender
- Employment
- Marital status
- Property area
- Employer category
- Loan purpose

The application returns:

**Loan Prediction + Approval Probability**

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **Scikit-learn**
- **Joblib**
- **Jupyter Notebook**
- **Streamlit**
- **Git & GitHub**
- **Streamlit Community Cloud**

---

## 📂 Project Structure

```text
CreditwiseLoanApproval/
│
├── app.py
├── main.ipynb
├── loan_approval_data.csv
├── model.pkl
├── preprocessing.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/shriihphoria/CreditwiseLoanApproval.git
cd CreditwiseLoanApproval
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

**[Launch CreditWiseLoan →](https://creditwiseloanapproval-7xznu2eursfhfzrswihvqc.streamlit.app/)**

---

## 🔮 Future Improvements

- [ ] Hyperparameter tuning
- [ ] Cross-validation
- [ ] Feature importance & model explainability
- [ ] Probability calibration
- [ ] Additional ML models
- [ ] Larger and more diverse dataset
- [ ] Fairness and bias evaluation
- [ ] Automated model testing

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes only**.

The predictions should not be used as real-world financial or lending decisions. Production lending systems require additional validation, explainability, fairness testing, security, and regulatory compliance.

---

## 👩‍💻 Author

**Shreeya Chakraborty**

**[GitHub Repository](https://github.com/shriihphoria/CreditwiseLoanApproval)**

**[Live Streamlit App](https://creditwiseloanapproval-7xznu2eursfhfzrswihvqc.streamlit.app/)**

---

<div align="center">

⭐ If you found this project interesting, consider giving the repository a star!

</div>
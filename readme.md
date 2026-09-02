<div align="center">

#  CreditWiseLoan — Loan Approval Prediction

**An End-to-End Machine Learning Project for Loan Approval Prediction**


</div>

---

##  Project Overview

**CreditWiseLoan** is a machine learning project designed to predict whether a loan application will be **approved** or **rejected**, based on an applicant's financial, personal, and employment-related information.

The project follows a complete, end-to-end ML workflow — from data exploration and preprocessing to model training, evaluation, and prediction — with the goal of understanding how various applicant and financial factors influence loan approval decisions.

---

##  Problem Statement

Loan approval decisions typically depend on a combination of factors, including:

- Applicant Income
- Coapplicant Income
- Credit Score
- Existing Loans
- Debt-to-Income Ratio
- Savings
- Collateral Value
- Employment Status
- Education Level
- Property Area
- Loan Purpose

Using these features, this project predicts the target variable: **`Loan_Approved`**

---

##  Project Structure

```
CreditwiseLoanApproval/
├── loanapprovaldata.csv    # Dataset used for training and analysis
├── main.ipynb               # Data preprocessing, EDA, model training,
│                             # evaluation, and prediction
└── README.md                 # Project documentation
```

###  Machine Learning Workflow

```
Raw Dataset
     │
     ▼
Data Exploration (EDA)
     │
     ▼
Data Cleaning
     │
     ▼
Handling Missing Values
     │
     ▼
Feature Encoding
     │
     ▼
Train-Test Split
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Loan Approval Prediction
```

---

##  Exploratory Data Analysis

The dataset was explored to understand the relationship between different features and loan approval outcomes. The analysis includes:

- Distribution of numerical features
- Analysis of categorical features
- Boxplots for detecting outliers
- Correlation analysis and heatmap
- Comparison of financial factors with loan approval status

> Visualizations were created using **Matplotlib** and **Seaborn**.

---

##  Data Preprocessing

The dataset was prepared for machine learning through the following steps:

- Handling missing values
- Encoding categorical variables
- Label encoding the target variable
- One-Hot Encoding categorical features
- Preparing numerical features
- Creating a machine-learning-ready dataset

---

##  Dataset Features

| Feature | Description |
|---|---|
| `Applicant_Income` | Income of the primary applicant |
| `Coapplicant_Income` | Income of the coapplicant |
| `Employment_Status` | Employment status of the applicant |
| `Age` | Age of the applicant |
| `Marital_Status` | Marital status |
| `Dependents` | Number of dependents |
| `Credit_Score` | Applicant's credit score |
| `Existing_Loans` | Number of existing loans |
| `DTI_Ratio` | Debt-to-Income ratio |
| `Savings` | Applicant's savings |
| `Collateral_Value` | Value of collateral |
| `Loan_Amount` | Requested loan amount |
| `Loan_Term` | Duration of the loan |
| `Loan_Purpose` | Purpose of the loan |
| `Property_Area` | Location category of the property |
| `Education_Level` | Education level of the applicant |
| `Gender` | Gender of the applicant |
| `Employer_Category` | Category of employer |

###  Target Variable

- **`Loan_Approved`** — Indicates whether a loan application is approved or not.

---

##  Machine Learning Models

Multiple classification models are trained and evaluated to identify the most effective approach for predicting loan approval. Models are compared using:

- **Accuracy**
- **Precision**
- **Recall**

This enables a clear comparison of model performance to determine which model performs best on the dataset.

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

##  How to Run the Project

**1. Clone the repository**
```bash
git clone https://github.com/shriihphoria/CreditwiseLoanApproval.git
```

**2. Navigate to the project directory**
```bash
cd CreditwiseLoanApproval
```

**3. Install the required libraries**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

**4. Start Jupyter Notebook**
```bash
jupyter notebook
```

Then open **`main.ipynb`** and run the cells.

---

##  Key Learning Outcomes

Through this project, practical experience was gained in:

- Data cleaning and preprocessing
- Handling missing values
- Exploratory data analysis
- Data visualization
- Feature encoding (Label Encoding & One-Hot Encoding)
- Train-test splitting
- Machine learning classification
- Model evaluation
- Comparing multiple ML models

---

##  Future Improvements

- [ ] Hyperparameter tuning using `GridSearchCV`
- [ ] Cross-validation
- [ ] Feature importance analysis
- [ ] Adding more machine learning models
- [ ] Building a Streamlit web application
- [ ] Deploying the trained model
- [ ] Creating a real-time loan prediction interface
- [ ] Adding a `requirements.txt` file

---

##  Disclaimer

This project is created for **educational and learning purposes only**. The model should **not** be used for real-world financial decision-making without proper validation, fairness testing, regulatory compliance, and additional production-level safeguards.

---

##  Author

**Shreeya Chakraborty**

---

<div align="center">

If you found this project interesting, consider giving the repository a ⭐️!

</div>
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="CreditWiseLoan",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# Load Model and Preprocessing
# --------------------------------------------------

model = joblib.load("model.pkl")
preprocessing = joblib.load("preprocessing.pkl")

ohe = preprocessing["ohe"]
scaler = preprocessing["scaler"]

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🏦 CreditWiseLoan")
st.subheader("Machine Learning Based Loan Approval Prediction")

st.write(
    "Enter the applicant's financial and personal information "
    "to predict the loan approval status."
)

st.divider()

# --------------------------------------------------
# Applicant Information
# --------------------------------------------------

st.header("👤 Applicant Information")

col1, col2, col3 = st.columns(3)

with col1:
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0.0,
        value=50000.0
    )

with col2:
    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0.0,
        value=0.0
    )

with col3:
    age = st.number_input(
        "Age",
        min_value=18.0,
        max_value=100.0,
        value=30.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    dependents = st.number_input(
        "Dependents",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

with col2:
    credit_score = st.number_input(
        "Credit Score",
        min_value=300.0,
        max_value=900.0,
        value=700.0
    )

with col3:
    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

# --------------------------------------------------
# Financial Information
# --------------------------------------------------

st.header("💰 Financial Information")

col1, col2, col3 = st.columns(3)

with col1:
    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        value=0.30,
        step=0.01
    )

with col2:
    savings = st.number_input(
        "Savings",
        min_value=0.0,
        value=50000.0
    )

with col3:
    collateral_value = st.number_input(
        "Collateral Value",
        min_value=0.0,
        value=100000.0
    )

col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=200000.0
    )

with col2:
    loan_term = st.number_input(
        "Loan Term",
        min_value=1.0,
        value=120.0
    )

# --------------------------------------------------
# Categorical Information
# --------------------------------------------------

st.header("📋 Applicant Details")

col1, col2, col3 = st.columns(3)

with col1:
    education = st.selectbox(
        "Education Level",
        ["Graduate", "Not Graduate"]
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col3:
    employment_status = st.selectbox(
        "Employment Status",
        [
            "Contract",
            "Salaried",
            "Self-employed",
            "Unemployed"
        ]
    )

col1, col2, col3 = st.columns(3)

with col1:
    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Single"]
    )

with col2:
    property_area = st.selectbox(
        "Property Area",
        ["Rural", "Semiurban", "Urban"]
    )

with col3:
    employer_category = st.selectbox(
        "Employer Category",
        [
            "Business",
            "Government",
            "MNC",
            "Private",
            "Unemployed"
        ]
    )

loan_purpose = st.selectbox(
    "Loan Purpose",
    [
        "Business",
        "Car",
        "Education",
        "Home",
        "Personal"
    ]
)

st.divider()

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button(
    "🔮 Predict Loan Approval",
    use_container_width=True
):

    # Education encoding
    # LabelEncoder alphabetical ordering:
    # Graduate = 0
    # Not Graduate = 1

    education_encoded = 0 if education == "Graduate" else 1

    # Create categorical input DataFrame
    categorical_input = pd.DataFrame({
        "Gender": [gender],
        "Employment_Status": [employment_status],
        "Marital_Status": [marital_status],
        "Property_Area": [property_area],
        "Employer_Category": [employer_category],
        "Loan_Purpose": [loan_purpose]
    })

    # One-hot encode using the SAME fitted encoder
    encoded_array = ohe.transform(categorical_input)

    encoded_df = pd.DataFrame(
        encoded_array,
        columns=ohe.get_feature_names_out(),
        index=[0]
    )

    # Create numerical/engineered features
    numeric_df = pd.DataFrame({
        "Applicant_Income": [applicant_income],
        "Coapplicant_Income": [coapplicant_income],
        "Age": [age],
        "Dependents": [dependents],
        "Existing_Loans": [existing_loans],
        "Savings": [savings],
        "Collateral_Value": [collateral_value],
        "Loan_Amount": [loan_amount],
        "Loan_Term": [loan_term],
        "Education_Level": [education_encoded],
        "Credit_Score_sq": [credit_score ** 2],
        "DTI_Ratio_sq": [dti_ratio ** 2]
    })

    # Combine features
    input_df = pd.concat(
        [numeric_df, encoded_df],
        axis=1
    )

    # EXACT feature order used during model training
    feature_order = [
        "Applicant_Income",
        "Coapplicant_Income",
        "Age",
        "Dependents",
        "Existing_Loans",
        "Savings",
        "Collateral_Value",
        "Loan_Amount",
        "Loan_Term",
        "Education_Level",
        "Gender_Male",
        "Employment_Status_Salaried",
        "Employment_Status_Self-employed",
        "Employment_Status_Unemployed",
        "Marital_Status_Single",
        "Property_Area_Semiurban",
        "Property_Area_Urban",
        "Employer_Category_Government",
        "Employer_Category_MNC",
        "Employer_Category_Private",
        "Employer_Category_Unemployed",
        "Loan_Purpose_Car",
        "Loan_Purpose_Education",
        "Loan_Purpose_Home",
        "Loan_Purpose_Personal",
        "Credit_Score_sq",
        "DTI_Ratio_sq"
    ]

    input_df = input_df[feature_order]

    # Scale using the SAME fitted scaler
    input_scaled = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0][1]

    st.divider()

    # --------------------------------------------------
    # Result
    # --------------------------------------------------

    if prediction == 1:

        st.success("### ✅ Loan Likely to be APPROVED")

        st.metric(
            "Approval Probability",
            f"{probability * 100:.2f}%"
        )

    else:

        st.error("### ❌ Loan Likely to be REJECTED")

        st.metric(
            "Approval Probability",
            f"{probability * 100:.2f}%"
        )

    st.caption(
        "This prediction is generated by the trained "
        "CreditWiseLoan Logistic Regression model."
    )
import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load trained Decision Tree model (update path if needed)
model = joblib.load("decision_tree_model.pkl")  # Make sure this matches your saved file

# UI Setup
st.set_page_config(page_title="Loan Approval Predictor", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.markdown("Use this tool to predict whether a loan will be approved based on applicant details.")

st.markdown("---")
st.subheader("📋 Enter Applicant Details")

# --- Input Fields ---
no_of_dependents = st.number_input("no_of_dependents", min_value=0)
education = st.selectbox("🎓 Education Level", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("💼 Self Employed", ["No", "Yes"])

income_annum = st.number_input("💰 Annual Income (₹)", min_value=10000, max_value=100000000, step=10000)
loan_amount = st.number_input("📦 Loan Amount (₹)", min_value=10000, max_value=100000000, step=1000)
loan_term = st.number_input("📅 Loan Term (Months)", min_value=6, max_value=360, step=6)
cibil_score = st.slider("📊 CIBIL Score", 300, 900, 700)

residential_assets_value = st.number_input("🏠 Residential Assets Value (₹)", min_value=0)
commercial_assets_value = st.number_input("🏢 Commercial Assets Value (₹)", min_value=0)
luxury_assets_value = st.number_input("🚗 Luxury Assets Value (₹)", min_value=0)
bank_asset_value = st.number_input("🏦 Bank Asset Value (₹)", min_value=0)

# --- Encoding categorical variables ---
education_encoded = 1 if education == "Graduate" else 0
self_employed_encoded = 1 if self_employed == "Yes" else 0

# Prepare input for prediction
input_data = np.array([[
    no_of_dependents, education_encoded, self_employed_encoded,
    income_annum, loan_amount, loan_term, cibil_score,
    residential_assets_value, commercial_assets_value,
    luxury_assets_value, bank_asset_value,
]])

# --- Prediction ---
if st.button("🔮 Predict Loan Approval"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")


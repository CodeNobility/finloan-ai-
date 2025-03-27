# 🏦 Loan Prediction Model

## 📌 Project Overview
This project aims to build a **Loan Prediction Model** using **Machine Learning** to help banks determine whether a loan applicant should be approved or not. The model is trained on historical loan application data and predicts the loan status (`Approved` or `Rejected`).

## 📂 Dataset Information
- The dataset contains details about **loan applicants**, such as:
  - `Gender`
  - `Married`
  - `Dependents`
  - `Education`
  - `Self_Employed`
  - `ApplicantIncome`
  - `CoapplicantIncome`
  - `LoanAmount`
  - `Loan_Amount_Term`
  - `Property_Area`
  - `Loan_Status` (Target Variable: `Y/N`)

## 🔧 Tools & Technologies Used
- **Programming Language:** Python 🐍  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **ML Model:** Decision Tree 
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score  

## 🚀 Model Building Steps
1️⃣ **Problem Understanding & Data Collection**  
   - Understanding business requirements  
   - Collecting relevant dataset  

2️⃣ **Data Preprocessing**  
   - Handling missing values  
   - Encoding categorical variables  
   - Feature scaling (if needed)  

3️⃣ **Train-Test Split & Cross-Validation**  
   - Splitting dataset into `Train (80%)` & `Test (20%)`  
   - Using `StratifiedKFold` for better validation  

4️⃣ **Model Selection & Training**  
   - Training **Decision Tree** models  
   - Tuning hyperparameters using `GridSearchCV`, `RandomizedSearchCV=`

5️⃣ **Model Evaluation**  
   - **Classification Metrics:**  
     - Accuracy  
     - Precision  
     - Recall  
     - F1-score  
   - Confusion Matrix analysis  

## 📊 Results & Insights
- **Model:** Decision Tree  
- **Accuracy Achieved:** 97.7%  

## 📢 Credits
Developed by **Prince Kumar Gupta**  

## 📞 Contact
📧 Email: princegupta1726@gmail.com  
🔗 GitHub: CodeNobility 



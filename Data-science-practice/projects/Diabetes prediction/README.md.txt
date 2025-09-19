Diabetes Prediction using Machine Learning
---
**Project Overview

This project aims to build a machine learning model that can predict whether a patient has diabetes based on diagnostic medical information. The dataset used is the Pima Indians Diabetes Dataset, which contains health-related features such as glucose level, BMI, age, etc.

The goal is to assist healthcare professionals by providing a data-driven tool for early detection of diabetes.

---
**Dataset

Source: Pima Indians Diabetes Database (commonly found on Kaggle / UCI ML repository).

Rows: 768

Features: 8 input features + 1 target variable

Target:

1 → Patient has diabetes

0 → Patient does not have diabetes

Features include:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

---

**Dependencies/ Librariries

Python

Pandas, NumPy → data handling

Matplotlib, Seaborn → visualization

Scikit-learn → model training & evaluation

---

**Workflow / Steps taken

Data Preprocessing

Handle missing values

Feature scaling (normalization/standardization)

Split into train & test sets

Exploratory Data Analysis (EDA)

Visualize feature distributions

Check correlation matrix & feature importance

---
**Model Training

Support Vector Machine (SVM)

Compare models based on accuracy, precision, recall, F1-score

---

**Model Evaluation

Accuracy scores

---
**Results

Best performing model achieved ~77% accuracy on the test set.

The model shows potential in predicting diabetes risk but should be used as a supporting tool, not as a replacement for medical diagnosis.

--

**How to Run

Clone this repository:

git clone https://github.com/username/diabetes-prediction.git
cd diabetes-prediction


Install dependencies:

pip install -r requirements.txt


Run the notebook or Python script:

jupyter notebook diabetes_prediction.ipynb


---
**Future Improvements

Explorin other model trainings and evaluations

Hyperparameter tuning for better performance

Try deep learning models (e.g., Neural Networks)

Deploy the model using Flask / Streamlit for a web-based app

---

**Acknowledgments

UCI Machine Learning Repository

Kaggle Dataset
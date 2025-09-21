California House Price Prediction

**Predicting median house values in California using Machine Learning 

🔹 Dataset: California Housing (from Scikit-learn)
🔹 Model: XGBoost Regressor
🔹 Goal: Understand the impact of features like income, house age, and population on housing prices

 Includes exploratory data analysis, visualizations, and model evaluation.

---

**Project Overview

This project applies the California Housing Dataset to predict median house values. The focus is on training an XGBoost Regressor, a powerful gradient boosting algorithm, to capture complex relationships in the data.

The project also explores the dataset through data visualization, feature analysis, and performance evaluation to identify the most important predictors of housing prices.

--- 

**Dataset

Source: California Housing Dataset (sklearn.datasets.fetch_california_housing)

Rows: 20,640

Features: 8 numerical features

Target: MedHouseVal → Median house value (in $100,000s)

Features include:

MedInc → Median income in block group

HouseAge → Median house age

AveRooms → Average number of rooms per household

AveBedrms → Average number of bedrooms per household

Population → Block group population

AveOccup → Average household occupancy

Latitude → Location (north-south)

Longitude → Location (east-west)


---

**Dependencies/Libraries

Python 

Pandas, NumPy → Data handling

Matplotlib, Seaborn → Visualization

Scikit-learn → Preprocessing, train-test split, evaluation metrics

XGBoost → Regression model

---

**Workflow

1.Data Loading

-Import dataset using fetch_california_housing from Scikit-learn.

2.Exploratory Data Analysis (EDA)

-Summary statistics

-Correlation matrix heatmap

-Distribution plots of key features

3.Data Preprocessing

-Handle scaling if needed

-Train-test split (80-20)

4.Model Training

-Use XGBoost Regressor

-Fit model on training data

5.Model Evaluation

-Evaluate using R² Score and Mean Squared Error (MSE)

-Compare training vs. test performance

6.Feature Importance

-Extract feature importance from the XGBoost model

-Visualize the most influential predictors

7.Prediction

-Predict house values on test data

-Compare predicted vs. actual values with scatter plot

---

**Results

-XGBoost Regressor provided strong predictive performance

-Key drivers of house prices:

 i)Median Income (strongest factor)

 ii)House Age

 iii)Latitude & Longitude (geographical influence)

---

**Future Improvements

-Hyperparameter tuning (GridSearchCV, RandomizedSearchCV)

-Try alternative models (Random Forest, Neural Networks)

-Deploy the model as a simple web app (Flask/Streamlit)

**With this project, we show how machine learning can be applied to real-world housing price prediction problems.
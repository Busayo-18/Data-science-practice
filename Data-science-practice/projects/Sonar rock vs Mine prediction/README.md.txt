# Sonar rock vs mine prediction


##Project Overview

This project uses the Sonar Dataset from the UCI Machine Learning Repository to build a classification model that can distinguish between:

Rock (R) → sonar signals reflected off rocks

Mine (M) → sonar signals reflected off metal cylinders (mines)

The dataset contains 208 samples, each with 60 numerical features representing the energy levels of sonar signals at different frequencies.

---

## Dataset

Source: UCI Machine Learning Repository – Sonar Dataset

Features:

60 real-valued attributes (continuous numbers between 0.0 and 1.0).

Target:

R → Rock

M → Mine



## Project Workflow/Steps

-Data Loading & Exploration

Load the dataset into a Pandas DataFrame.

Explore feature distributions and target balance.

-Preprocessing

Encode categorical labels (R → 0, M → 1).

Normalize/scale features if needed.

Split dataset into train and test sets.

-Model Building

using logical regression model

Tune hyperparameters for better performance.

-Evaluation

Accuracy, Precision, Recall.


-Prediction

Input a sonar signal (60 values) and predict whether it is a Rock or Mine.


##Dependencies used Used

Python

Pandas, NumPy → Data handling

Scikit-learn → ML models & preprocessing




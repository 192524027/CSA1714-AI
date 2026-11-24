"""
Experiment 30: Linear Regression Algorithm
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Independent (x) and Dependent (y) variables
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

# Initialize and fit Linear Regression model
model = LinearRegression()
model.fit(x, y)

# Predict for new input x = 6
prediction = model.predict([[6]])

print("Linear Regression Model")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted value:", prediction[0])

"""
Experiment 31: K-Nearest Neighbors (KNN) Classification
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from sklearn.neighbors import KNeighborsClassifier

# Feature coordinates and target class labels
x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

# Initialize and fit KNN classifier with k=3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

# Predict class for test point (5, 6)
test_point = [[5, 6]]
prediction = model.predict(test_point)

print("K-Nearest Neighbors (KNN) Classifier")
print("Training Samples:", x)
print("Class Labels:", y)
print("Predicted Class:", prediction[0])

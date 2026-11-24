"""
Experiment 32: Decision Tree Classifier
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from sklearn.tree import DecisionTreeClassifier

# Feature dataset and target classes
x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

# Initialize Decision Tree model and train
model = DecisionTreeClassifier()
model.fit(x, y)

# Test sample evaluation
test_point = [[5, 6]]
prediction = model.predict(test_point)

print("Decision Tree Classification")
print("Training Features:", x)
print("Class Labels:", y)
print("Predicted Class:", prediction[0])

"""
Experiment 35: Support Vector Machine (SVM) Classification
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from sklearn.svm import SVC

# Feature dataset
x = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = [0, 0, 0, 1, 1, 1]

# Linear SVM Classifier
model = SVC(kernel='linear')
model.fit(x, y)

test_sample = [[5, 6]]
prediction = model.predict(test_sample)

print("Support Vector Machine (SVM) Classification")
print("Kernel: Linear")
print("Predicted Class:", prediction[0])

"""
Experiment 36: Principal Component Analysis (PCA) Dimensionality Reduction
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Input 2D dataset
x = [[2, 4], [3, 5], [4, 6], [5, 8], [6, 9]]

# Standardize features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Reduce from 2D to 1D using PCA
pca = PCA(n_components=1)
result = pca.fit_transform(x_scaled)

print("Original Data:")
print(x)
print("Reduced Data:")
print(result)

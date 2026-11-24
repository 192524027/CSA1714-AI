"""
Experiment 38: K-Means Clustering Algorithm
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from sklearn.cluster import KMeans

# 2D data points
x = [[1, 2], [2, 3], [3, 3],
     [8, 8], [9, 8], [8, 9]]

model = KMeans(n_clusters=2, random_state=0, n_init=10)
model.fit(x)

print("Cluster Labels:")
print(model.labels_)
print("Cluster Centers:")
print(model.cluster_centers_)

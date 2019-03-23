import kmeans as km
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,10))
sns.set()

from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=.8, random_state=0)

clusters, centers, k = km.elbow_kmeans(X, 10)
#print(k)
plt.scatter(X[:, 0], X[:, 1], s=50, c=clusters, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='*', c='g', s=150)
plt.show()
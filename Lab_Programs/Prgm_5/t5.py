import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# Load dataset from CSV
data = pd.read_csv("housing.csv")
X = data.values  # Convert to NumPy array
X = pd.get_dummies(data)  # Converts categorical columns to numeric dummy variables

# K-Means clustering
k = 3  # choose number of clusters
kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
labels_kmeans = kmeans.labels_

# EM clustering (Gaussian Mixture)
gmm = GaussianMixture(n_components=k, random_state=42).fit(X)
labels_gmm = gmm.predict(X)

# Compare clustering quality using silhouette score
score_kmeans = silhouette_score(X, labels_kmeans)
score_gmm = silhouette_score(X, labels_gmm)

print("K-Means Silhouette Score:", score_kmeans)
print("EM (GMM) Silhouette Score:", score_gmm)

if score_kmeans > score_gmm:
    print("✅ K-Means produced better clusters.")
else:
    print("✅ EM (GMM) produced better clusters.")

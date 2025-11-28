from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load image dataset (handwritten digits)
digits = load_digits()
X, y = digits.data, digits.target  # Flattened image pixels and labels
print(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train KNN
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)

# Predict and check accuracy
print("Accuracy:", knn.score(X_test, y_test))

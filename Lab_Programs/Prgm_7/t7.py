import pandas as pd
from surprise import SVD, Dataset, accuracy
from surprise.model_selection import train_test_split

data = Dataset.load_builtin('ml-100k')
raw_ratings = data.raw_ratings
df = pd.DataFrame(raw_ratings, columns=['user', 'item', 'rating', 'timestamp'])
rating_matrix = df.pivot_table(index='user', columns='item', values='rating')
print("User–Item Rating Matrix:")
print(rating_matrix)
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
model = SVD()
model.fit(trainset)
predictions = model.test(testset)
print("\nRMSE on Test Data:")
rmse = accuracy.rmse(predictions)
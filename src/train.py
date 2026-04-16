import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import joblib

# Load data
data = pd.read_csv("../data/labeled_data.csv")

X = data[['distance','accel','jerk','speed']]
y = data['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Models
dt = DecisionTreeClassifier(max_depth=5)
knn = KNeighborsClassifier(n_neighbors=3)
nb = GaussianNB()

# Ensemble
model = VotingClassifier(
    estimators=[('dt', dt), ('knn', knn), ('nb', nb)],
    voting='hard'
)

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "../models/ensemble_model.pkl")

print("Model trained & saved ")
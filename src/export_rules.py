from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

data = pd.read_csv("../data/labeled_data.csv")

X = data[['distance','accel','jerk','speed']]
y = data['label']

model = DecisionTreeClassifier(max_depth=5)
model.fit(X, y)

rules = export_text(model, feature_names=list(X.columns))

with open("../models/rules.txt","w") as f:
    f.write(rules)

print("Rules exported ✅")
print(rules)
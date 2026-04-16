import pandas as pd

data = pd.read_csv("../data/raw_log.csv")

# simple rule-based labeling
def label(row):
    if row['distance'] < 20:
        return 4  # STOP
    elif row['distance'] < 40:
        return 1  # SLOW
    elif row['jerk'] > 2:
        return 1  # SLOW
    else:
        return 0  # SAFE

data['label'] = data.apply(label, axis=1)

# save
data[['distance','accel','jerk','speed','label']].to_csv(
    "../data/labeled_data.csv", index=False)

print("Preprocessing done ✅")
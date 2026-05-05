import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

df = pd.read_csv("data/house_data.csv")

tier_1 = ["Mumbai", "Pune", "Noida"]
tier_2 = ["Bhopal", "Indore", "Jabalpur"]

def city_score(city):
    if city in tier_1:
        return 2
    elif city in tier_2:
        return 1
    else:
        return 0

df["city_score"] = df["location"].apply(city_score)

df.drop(["location"], axis=1, inplace=True)

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=400,
    max_depth=25,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))

os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/model.pkl", "wb"))

print("✅ Model trained successfully")
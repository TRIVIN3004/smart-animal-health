import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("animal_data.csv")

# Simple rule-based label generation
def label_health(row):
    if row["Temperature"] > 39.0 or row["HeartRate"] > 100:
        return "Sick"
    elif row["Activity"] < 2:
        return "Low Activity"
    else:
        return "Healthy"

df["HealthStatus"] = df.apply(label_health, axis=1)

X = df[["Temperature", "HeartRate", "Activity"]]
y = df["HealthStatus"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

joblib.dump(model, "animal_health_model.pkl")
print("Model saved!")

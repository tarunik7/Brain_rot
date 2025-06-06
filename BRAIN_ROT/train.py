import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load the synthetic dataset
df = pd.read_csv("synthetic_dataset.csv")

# Features and label
X = df.drop("addicted", axis=1)
y = df["addicted"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate performance
y_pred = model.predict(X_test)
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, "brainrot_model.pkl")
print("\n✅ Model saved as brainrot_model.pkl")

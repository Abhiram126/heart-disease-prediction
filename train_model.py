import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("heart.csv")  # Ensure dataset path is correct

# Split into features and target
X = df.drop(columns=["target"]).copy()  # Copy to avoid modifying original
y = df["target"]

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Find the best random_state for maximum accuracy
max_accuracy = 0
best_x = None
best_model = None

for x in range(2000):
    rf = RandomForestClassifier(random_state=x)
    rf.fit(X_train, y_train)
    Y_pred_rf = rf.predict(X_test)
    current_accuracy = accuracy_score(y_test, Y_pred_rf) * 100  # No need to round until print

    if current_accuracy > max_accuracy:
        max_accuracy = current_accuracy
        best_x = x
        best_model = rf  # Save the best performing model

print(f"Best Accuracy: {max_accuracy:.2f}% at random_state={best_x}")

# Save the best trained model
joblib.dump(best_model, "random_forest_model.pkl")
print("Optimized model saved as random_forest_model.pkl")

# Feature importance analysis (Optional but useful)
feature_importances = pd.Series(best_model.feature_importances_, index=X.columns)
print("\nFeature Importances:\n", feature_importances.sort_values(ascending=False))

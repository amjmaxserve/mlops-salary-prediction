import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

# -----------------------------
# Generate Synthetic Dataset
# -----------------------------

np.random.seed(42)

num_samples = 1000

ages = np.random.randint(21, 60, num_samples)

education = np.random.choice([
    'Bachelors',
    'Masters',
    'PhD',
    'Diploma'
], num_samples)

hours_per_week = np.random.randint(20, 60, num_samples)

occupation = np.random.choice([
    'Engineer',
    'Teacher',
    'Manager',
    'Developer',
    'Analyst'
], num_samples)

experience = np.random.randint(1, 35, num_samples)

salary = []

for i in range(num_samples):
    if (
        experience[i] > 10 and
        hours_per_week[i] > 40 and
        education[i] in ['Masters', 'PhD']
    ):
        salary.append('>50K')
    else:
        salary.append('<=50K')

# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame({
    'age': ages,
    'education': education,
    'hours_per_week': hours_per_week,
    'occupation': occupation,
    'experience': experience,
    'salary': salary
})

print("\nGenerated Dataset Head:\n")
print(df.head())

print("\nDataset Info:\n")
df.info()

# -----------------------------
# Encode Categorical Features
# -----------------------------

categorical_features = ['education', 'occupation']
label_encoders = {}

for col in categorical_features:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

print("\nEncoded Dataset Head:\n")
print(df.head())

# -----------------------------
# Encode Target Variable
# -----------------------------

target_encoder = LabelEncoder()
df['salary'] = target_encoder.fit_transform(df['salary'])

# -----------------------------
# Split Features and Labels
# -----------------------------

X = df.drop('salary', axis=1)
y = df['salary']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:\n")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------

import os
os.makedirs('model', exist_ok=True)

joblib.dump(model, 'model/salary_model.pkl')
joblib.dump(label_encoders, 'model/label_encoders.pkl')
joblib.dump(target_encoder, 'model/target_encoder.pkl')

print("\nModel Saved Successfully!\n")
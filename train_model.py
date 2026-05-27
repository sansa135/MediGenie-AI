import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Create models folder
os.makedirs("models", exist_ok=True)

# Load dataset
train_df = pd.read_csv('dataset/Training.csv')

# Remove extra column
if 'Unnamed: 133' in train_df.columns:
    train_df = train_df.drop('Unnamed: 133', axis=1)

# Features and target
X = train_df.drop('prognosis', axis=1)
y = train_df['prognosis']

# Encode diseases
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save files
joblib.dump(model, 'models/medical_model.pkl')
joblib.dump(encoder, 'models/label_encoder.pkl')
joblib.dump(list(X.columns), 'models/symptom_columns.pkl')

print("Advanced Medical AI Model Trained Successfully!")
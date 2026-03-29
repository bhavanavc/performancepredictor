import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load data
data = pd.read_csv("data.csv")

# Split features and target
X = data[["study_hours", "attendance", "sleep_hours"]]
y = data["performance"]

# Convert labels (Good/Average/Poor → numbers)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Function to predict
def predict_performance(study, attendance, sleep):
    prediction = model.predict([[study, attendance, sleep]])
    return le.inverse_transform(prediction)[0]
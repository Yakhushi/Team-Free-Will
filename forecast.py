import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("../backend/noise_data.csv", names=["timestamp", "location", "dB"])
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.weekday

X = df[['hour', 'weekday']]
y = df['dB']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

# Predict for next hour
from datetime import datetime
import numpy as np

now = datetime.now()
prediction = model.predict(np.array([[now.hour + 1, now.weekday()]]))
print(f"Predicted dB next hour: {prediction[0]:.2f}")


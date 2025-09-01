
# src/model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def train_model(df):
    X = df[['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed']]
    y = df['PM2.5']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    joblib.dump(model, 'output/model.pkl')
    return model

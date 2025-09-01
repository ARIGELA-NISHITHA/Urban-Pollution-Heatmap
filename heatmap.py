
# src/heatmap.py
import folium
from folium.plugins import HeatMap
import pandas as pd
import joblib

def generate_heatmap(df):
    model = joblib.load('output/model.pkl')
    features = df[['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed']]
    df['PM2.5_pred'] = model.predict(features)

    heat_data = [[row['latitude'], row['longitude'], row['PM2.5_pred']] for _, row in df.iterrows()]

    m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=12)
    HeatMap(heat_data).add_to(m)
    m.save("output/pollution_heatmap.html")



# src/preprocess.py
import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    df = df.dropna()
    return df

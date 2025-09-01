Jupyter Notebook (EDA_and_Model.ipynb)

You can include a Jupyter notebook for exploration, training, and calling the heatmap script:

from src.preprocess import load_data
from src.model import train_model
from src.heatmap import generate_heatmap

df = load_data('data/pollution_data.csv')
model = train_model(df)
generate_heatmap(df)

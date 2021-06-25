from google.colab import files
uploaded = files.upload()

import pandas as pd 
datos_maraton = pd.read_csv('MarathonData.csv')
datos_maraton

datos_maraton['CrossTraining']

datos_maraton.dropna(subset=["CrossTraining"])
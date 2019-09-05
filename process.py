import pandas as pd
import numpy as np

def get_data():
    df = pd.read_csv("test.csv")
    Y = df["Font"].values
    df.drop(columns = ["Font"])
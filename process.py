import pandas as pd
import numpy as np

def get_data():
    df = pd.read_csv("test.csv")
    Y = df["Font"].values
    df = df.drop(columns = ["Font"])
    X = df.values

    X = X.astype('float32') 

    X[:,0] = (X[:,0] - X[:,0].mean())/X[:, 0].std()
    X[:,1] = (X[:,1] - X[:,1].mean())/X[:, 1].std()
    X[:,2] = (X[:,2] - X[:,2].mean())/X[:, 2].std()

    return X, Y
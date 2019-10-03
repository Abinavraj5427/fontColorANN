import pandas as pd
import numpy as np


def get_data():
    df = pd.read_csv("test.csv")
    Y = df["Font"].values
    df = df.drop(columns = ["Font"])
    X = df.values

    X = X.astype('float32') 
    X_orig = X
    X[:,0] = (X[:,0] - X[:,0].mean())/X[:, 0].std()
    X[:,1] = (X[:,1] - X[:,1].mean())/X[:, 1].std()
    X[:,2] = (X[:,2] - X[:,2].mean())/X[:, 2].std()

    return X, Y.reshape((Y.shape[0], 1))

def process_data(X_raw):
    df = pd.read_csv("test.csv")
    Y = df["Font"].values
    df = df.drop(columns = ["Font"])
    X = df.values

    X = X.astype('float32') 
    X_orig = X

    X_raw = X_raw.astype('float32') 
    X_raw[0] = (X_raw[0] - X_orig[:,0].mean())/X_orig[:, 0].std()
    X_raw[1] = (X_raw[1] - X_orig[:,1].mean())/X_orig[:, 1].std()
    X_raw[2] = (X_raw[2] - X_orig[:,2].mean())/X_orig[:, 2].std()
    return X_raw
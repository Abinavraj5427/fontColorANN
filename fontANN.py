import numpy as np
from process import get_data

def binary_cross_entropy():
    

def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def feedforward(X, W1, W2, B1, B2):
    A1 = X.dot(W1) + B1
    Z = sigmoid(A1)
    A2 = Z.dot(W2) + B2
    return sigmoid(A2)

def class_rate(YP, Y):
    rate = 0
    return rate

X, Y = get_data()

D = X.shape[1]
M = 3
K = 1 

W1 = np.random.randn(D, M)
B1 = np.random.randn(M)
W2 = np.random.randn(M, K)
B2 = np.random.randn(K)

YP = feedforward(X, W1, W2, B1, B2)


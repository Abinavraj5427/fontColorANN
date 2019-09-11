import numpy as np
from process import get_data

def binary_cross_entropy(Y, T):
    return T.dot(np.log(Y)) + (1-T).dot(np.log(1-Y))

def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def feedforward(X, W1, W2, B1, B2):
    A1 = X.dot(W1) + B1
    Z = sigmoid(A1)
    A2 = Z.dot(W2) + B2
    return sigmoid(A2), A1, A2

def class_rate(YP, Y):
    rate = 0
    return rate

def gradient_w2(Y, T, Z2, A2):
    return A2.T.dot(((T - Y)/(T - T * T)) * Z2 * (1 - Z2)).sum(axis = 0) 

def gradient_w1(Y, T, Z2, W2, Z1, X):
    dw2 =  W2.dot(((T - Y)/(T - T * T)) * Z2 * (1 - Z2))
    return X.dot(dw2  * Z1 * (1 - Z1))

def gradient_b2(Y, T, Z):
    return (((T - Y)/(T - T * T)) * Z * (1 - Z)).sum(axis = 0)

def gradient_b1(Y, T, Z2, W2, Z1):
    dw2 =  W2.dot(((T - Y)/(T - T * T)) * Z2 * (1 - Z2))
    return np.sum(dw2  * Z1 * (1 - Z1), axis = 0)   

X, Y = get_data()

D = X.shape[1]
M = 3
K = 1 

W1 = np.random.randn(D, M)
B1 = np.random.randn(M)
W2 = np.random.randn(M, K)
B2 = np.random.randn(K)

YP = feedforward(X, W1, W2, B1, B2)

train_size = .85
epochs = batch_size = 50000


X_train = X[:(int)(X.shape[0] *train_size),:]
X_test = X[(int)(X.shape[0] *train_size):,:]
Y_train =  Y[:(int)(X.shape[0] *train_size),:]
Y_test = Y[(int)(X.shape[0] *train_size):,:] 

X_batch = np.split(X_train, batch_size)
Y_batch = np.split(Y_train, batch_size)

learning_rate = 1e-7

for epoch in range(epochs):
    X = X_batch[epoch]
    Y = Y_batch[epoch]

    YP, Z1, Z2 = feedforward(X, W1, W2, B1, B2)


    W1 = learning_rate * gradient_w1(YP, Y, Z2, W2, Z1, X)
    W2 = learning_rate * gradient_w2(YP, Y, Z2, A2)
    B1 = learning_rate * 
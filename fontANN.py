import numpy as np
import matplotlib.pyplot as plt
from process import get_data

def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def feedforward(X, W1, W2, B1, B2):
    A1 = X.dot(W1) + B1 #N x M
    Z = sigmoid(A1) #N x M
    A2 = Z.dot(W2) + B2 # N x K
    Z2 = sigmoid(A2) #N x K
    return Z2, Z

def gradient_w1 (Y, T, Z2, W2, Z1, X):
    dw2 =  ((gradient_BCE(Y, T)) * Z2 * (1 - Z2)).dot(W2.T) #N x M
    return X.T.dot(dw2  * Z1 * (1 - Z1))

def gradient_w2(Y, T, Z2, Z1):
    return Z1.T.dot((gradient_BCE(Y, T)) * Z2 * (1 - Z2))

def gradient_b2(Y, T, Z):
    return ((gradient_BCE(Y, T)) * Z * (1 - Z)).sum(axis = 0)

def gradient_b1(Y, T, Z2, W2, Z1):
    dw2 =  ((gradient_BCE(Y, T)) * Z2 * (1 - Z2)).dot(W2.T)
    return np.sum(dw2  * Z1 * (1 - Z1), axis = 0)

def class_rate(Y, T):
	correct = 0
	for i in range(len(Y)):
		if(T[i] == Y[i]):
			correct = correct+1

	class_rate = correct/len(Y)
	return class_rate

def loss(Y, T):
    return (T * np.log(Y) + (1 - T) * np.log(1 - Y)).sum()

def gradient_BCE(Y, T):
    return (T/Y) - (1-T)/(1-Y)


X, Y = get_data()

D = X.shape[1]
M = 16
K = 1 

W1 = np.random.randn(D, M) #3 x 3
B1 = np.random.randn(M) #3
W2 = np.random.randn(M, K) #3 x 1
B2 = np.random.randn(K) #1


train_size = .85
epochs = batch_size = 50000


X_train = X[:(int)(X.shape[0] * train_size),:]
X_test = X[(int)(X.shape[0] * train_size):,:]
Y_train =  Y[:(int)(Y.shape[0] * train_size)]
Y_test = Y[(int)(Y.shape[0] * train_size):] 

X_batch = np.split(X_train, batch_size)
Y_batch = np.split(Y_train, batch_size)

learning_rate = 1e-5
losses = []
rates = []
for epoch in range(epochs):
    X = X_batch[epoch]
    Y = Y_batch[epoch]

    YP, Z1 = feedforward(X, W1, W2, B1, B2)
    Z2 = YP
    l = loss(YP, Y)
    losses.append(-l)
    LP = np.rint(YP)
    r = class_rate(LP, Y)
    rates.append(r)

    if(epoch % 1000 == 0):
        print("loss: {} class rate: {}".format(l, r))

    W2 += learning_rate * gradient_w2(YP, Y, Z2, Z1)
    B2 += learning_rate * gradient_b2(YP, Y, Z2)
    W1 += learning_rate * gradient_w1(YP, Y, Z2, W2, Z1, X)
    B1 += learning_rate * gradient_b1(YP, Y, Z2, W2, Z1)

plt.plot(losses)
plt.show()

plt.plot(rates)
plt.show()

Y, Z = feedforward(X_test, W1, W2, B1, B2)
r = class_rate(np.rint(Y), Y_test)
print("test-set class rate: ",r)
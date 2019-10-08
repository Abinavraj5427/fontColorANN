
import numpy as np
from process import process_data
from fontANN import feedforward
import sys

X = np.array([float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])])
X = process_data(X)
npzfile = np.load('matrix.npz')
W2 = npzfile['W2']
B2 = npzfile['B2']
W1 = npzfile['W1']
B1 = npzfile['B1']
Y, Z = feedforward(X, W1, W2, B1, B2)
print(int(np.rint(Y[0])))
# return 1
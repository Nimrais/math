import numpy as np

N = 100
X, Y = np.random.normal(loc = 0, size = (N, 1)), np.random.normal(loc = 0, size = (N, 1))

print(np.trace(X @ X.T @ Y @ Y.T))
print(np.trace(X.T @ Y @ (X.T @ Y).T))


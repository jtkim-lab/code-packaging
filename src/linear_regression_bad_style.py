"""
    theta = (X^T X)^{-1} X^T by
    y = theta^T bx
"""

import numpy as np


def theta(X, by):
    a=np.matmul(np.transpose(X), X)
    b = np.linalg.inv(a)
    c=np.matmul(b,np.transpose(X))
    d = np.matmul(c,by)
    return d

def pred(theta, X):
    a = np.matmul(X, theta)

    return a


if __name__ == '__main__':
    def target(X):
        return np.sum(10.0 * X, axis=1)

    X_train = np.random.uniform(-10, 10, 100)[..., np.newaxis]
    by_train = target(X_train) + np.random.randn(X_train.shape[0])

    X_test = np.linspace(-10, 10, 1001)[..., np.newaxis]
    by_test = target(X_test)

    a = theta(X_train, by_train)
    b = pred(a, X_test)

    print(a)
    print(np.sum((b - by_test)**2))

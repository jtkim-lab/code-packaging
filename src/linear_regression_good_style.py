"""
This is to implement linear regression.

"""
import numpy as np


def calculate_theta(X, by):
    """
    This function is to calculate a parameter vector using a closed-form solution.

    :param X: Input matrix.
    :type X: np.ndarray
    :param by: Output vector.
    :type by: np.ndarray

    :returns: Parameter vector.
    :rtype: np.ndarray

    """

    X_T_X = np.matmul(np.transpose(X), X)
    return np.matmul(np.matmul(np.linalg.inv(X_T_X), np.transpose(X)), by)

def predict(theta, X):
    """
    This function is to predict the output of input matrix given a parameter vector.

    :param theta: Parameter vector.
    :type theta: np.ndarray
    :param X: Input matrix.
    :type X: np.ndarray

    :returns: Output vector.
    :rtype: np.ndarray

    """

    return np.matmul(X, theta)


if __name__ == '__main__':
    def target(X):
        return np.sum(10.0 * X, axis=1)

    X_train = np.random.uniform(-10, 10, 100)[..., np.newaxis]
    by_train = target(X_train) + np.random.randn(X_train.shape[0])

    X_test = np.linspace(-10, 10, 1001)[..., np.newaxis]
    by_test = target(X_test)

    theta = calculate_theta(X_train, by_train)
    outputs_test = predict(theta, X_test)

    print(theta)
    print(np.sum((outputs_test - by_test)**2))

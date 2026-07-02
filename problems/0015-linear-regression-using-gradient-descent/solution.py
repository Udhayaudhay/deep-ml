import numpy as np

def linear_regression_gradient_descent(X, y, alpha, iterations):
    m, n = X.shape

    theta = np.zeros(n)

    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1 / m) * X.T.dot(errors)
        theta = theta - alpha * gradient

    return theta
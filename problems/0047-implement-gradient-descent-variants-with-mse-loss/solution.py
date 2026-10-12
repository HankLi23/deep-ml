import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    m = X.shape[0]
    n = X.shape[1]
    
    for _ in range(n_epochs):
        if method == "batch":
            predict = X @ weights
            gradient = (2/m)*X.T @ (predict - y)
            weights = weights - learning_rate * gradient
        
        elif method == "stochastic":
            for i in range(m):
                xi = X[i:i+1]
                yi = y[i:i+1]
                y_pred_i = xi @ weights
                gradient_i = 2*xi.T @ (y_pred_i - yi)
                weights = weights - learning_rate * gradient_i
                
        elif method == "mini_batch":
            for i in range(0, m, batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                b = X_batch.shape[0]
                y_pred_batch = X_batch @ weights
                gradient_batch = (2 / b) * X_batch.T @ (y_pred_batch - y_batch)
                weights = weights - learning_rate * gradient_batch
        
    return weights

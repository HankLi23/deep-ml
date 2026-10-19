import numpy as np

def pegasos_kernel_svm(data: np.ndarray, labels: np.ndarray, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0) -> tuple:
    """
    Train a kernel SVM using the deterministic Pegasos algorithm.
    
    Args:
        data: Training data of shape (n_samples, n_features)
        labels: Labels of shape (n_samples,) with values in {-1, 1}
        kernel: 'linear' or 'rbf'
        lambda_val: Regularization parameter
        iterations: Number of training iterations
        sigma: RBF kernel bandwidth (only used if kernel='rbf')
    
    Returns:
        Tuple of (alphas, bias) where alphas is a list and bias is a float
    """
    # Your code here
    n_samples, n_features = data.shape

    alphas = np.zeros(n_samples)
    bias = 0.0


    for t in range(1, iterations + 1):
        learning_rate = 1.0 /(lambda_val * t)
        for i in range(n_samples):
            xi = data[i]
            yi = labels[i]
            total = 0.0
            for j in range(n_samples):
                xj = data[j]
                yj = labels[j]
                total += alphas[j] * yj * kernel_function(kernel, xj, xi, sigma)
            gi = total + bias
            
            if yi * gi < 1:
                alphas[i] = alphas[i] + learning_rate*(1-lambda_val * alphas[i])
                bias = bias + learning_rate * yi
            else:
                alphas[i] = alphas[i] - learning_rate*lambda_val * alphas[i]
        
    return list(alphas), bias

def kernel_function(kernel, x, z, sigma):
    if kernel == 'linear':
        return x @ z
    
    return np.exp(-np.sum((x - z) ** 2)/(2 * sigma * sigma))
    

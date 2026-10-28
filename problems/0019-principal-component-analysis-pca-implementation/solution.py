import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    n_samples, n_features = data.shape

    mean = np.mean(data, axis = 0)
    std = np.std(data, axis = 0, ddof= 1)
    data_centered = (data-mean)/std

    matrix = (data_centered.T @ data_centered) / (n_samples - 1)

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)

    sort_idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sort_idx]
    eigenvectors = eigenvectors[:, sort_idx]

    top_k = eigenvectors[:, :k]

    for col in range(k):
        vec = top_k[:, col]
        for idx in range(len(vec)):
            if(abs(vec[idx]) > 1e-10):
                if vec[idx] < 0:
                    vec *= -1
                break

    result = np.round(top_k, 4)
    return result
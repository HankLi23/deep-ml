import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	num, D = X.shape
	result = []

	for i in range(num):
		z = X[i] @ weights + bias
		prob = 1/(1 + np.exp(-z))
		pred = 1 if prob >= 0.5 else 0
        result.append(pred)
	
	return np.array(result)


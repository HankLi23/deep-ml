import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_mat = np.array(X, dtype=np.float64)
    y_mat = np.array(y, dtype=np.float64)

	theta = (np.linalg.inv(X_mat.T @ X_mat)) @ X_mat.T @ y_mat

	theta_list = [round(float(val), 4) for val in theta]
    return theta_list

import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	mean = np.mean(y_true)

	SSR = np.sum((y_true - y_pred)**2)
	SST = np.sum((y_true - mean)**2)

	return 1 - (SSR/SST)

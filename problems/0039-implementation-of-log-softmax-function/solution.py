import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	z = np.array(scores)
	max_z = max(z)
	sum_z = np.sum(np.exp(z - max_z))
	log = np.log(sum_z)

	result = z - max_z - log
	return result

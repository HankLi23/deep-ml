import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	# if not v1:
	# 	return -1
	# if not v2:
	# 	return -1

	row1 = len(v1)
	row2 = len(v2)
	if row1 != row2:
		return -1
	
	dot = 0
	for i in range(row1):
		dot += v1[i] * v2[i]
	
	true1 = 0
	for i in range(row2):
		true1 += (v1[i]) ** 2
	true1 = np.sqrt(true1)

	true2 = 0
	for i in range(row2):
		true2 += (v2[i]) ** 2
	true2 = np.sqrt(true2)

	return dot / (true1 * true2)

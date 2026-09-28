import numpy as np

def calculate_dot_product(vec1, vec2):
	length = len(vec1)
	result = 0
	for i in range(length):
		result += vec1[i] * vec2[i]
	return  result
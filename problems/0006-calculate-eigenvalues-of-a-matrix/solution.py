import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix [1][0]
	tr = matrix[0][0] + matrix[1][1]

	res1 = (tr + math.sqrt(tr**2 - 4*det))/2
	res2 = (tr - math.sqrt(tr**2 - 4*det))/2

	result = []
	result.append(res1)
	result.append(res2)
	return result
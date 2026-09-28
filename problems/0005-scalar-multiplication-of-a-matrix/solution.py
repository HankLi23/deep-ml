def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	row = len(matrix)
	column = len(matrix[0])

	for i in range(row):
		for j in range(column):
			matrix[i][j] *= scalar
	
	return matrix
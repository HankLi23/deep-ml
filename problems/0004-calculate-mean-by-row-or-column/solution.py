def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	row = len(matrix)
	column = len(matrix[0])

	if mode == "row":
		result = []
		for i in range(row):
			add = 0
			for j in range(column):
				add += matrix[i][j]
			mean = add/column
			result.append(mean)

		return result
	else:
		result = []
		for j in range(column):
			add = 0
			for i in range(row):
				add += matrix[i][j]
			mean = add/row
			result.append(mean)

		return result
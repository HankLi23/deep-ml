def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if not a:
		return -1

	column = len(a[0])
	length = len(b)
	if column != length:
		return -1

	result = []

	for row in a:
		dot = 0
		for x, y in zip(row, b):
			dot += x*y
		result.append(dot)
	return result

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	feature = len(vectors)
	
	result = []
	for i in range(feature):
		row = []
		for j in range(feature):
			row.append(covariance(vectors[i], vectors[j]))
		result.append(row)

	return result

def mean(v):
        return sum(v) / len(v)

def covariance(vector1, vector2):
	num = len(vector1)
	mean1 = mean(vector1)
	mean2 = mean(vector2)
	sum = 0

	for i in range(num):
		sum += (vector1[i] - mean1) * (vector2[i] - mean2)
	
	return sum/(num - 1)
import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	num = len(y_pred)
	cnt = 0

	for i in range(num):
		if y_pred[i] == y_true[i]:
			cnt += 1
	acc = cnt/num
	return acc
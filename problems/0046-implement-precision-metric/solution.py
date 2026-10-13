import numpy as np
def precision(y_true, y_pred):
	# Your code here
	TP = 0
	FP = 0

	TP = np.sum((y_true == 1) & (y_pred == 1))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    
	if TP + FP ==0:
		return 0.0
    output = TP / (TP + FP)
    return output


from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	TP = 0
    FN = 0
    FP = 0
    TN = 0
    
    for y_true, y_pred in data:
        if y_true == 1 and y_pred == 1:
            TP +=1
        elif y_true ==1 and y_pred ==0:
            FN +=1
        elif y_true ==0 and y_pred ==1:
            FP +=1
        elif y_true ==0 and y_pred ==0:
            TN +=1
    
    matrix = [
        [TP, FN],
        [FP, TN]
    ]
    return matrix
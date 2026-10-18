
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	data = [actual, predicted]
	TP = 0
    FN = 0
    FP = 0
    TN = 0
    
    for y_true, y_pred in zip(actual, predicted):
        if y_true == 1 and y_pred == 1:
            TP +=1
        elif y_true ==1 and y_pred ==0:
            FN +=1
        elif y_true ==0 and y_pred ==1:
            FP +=1
        elif y_true ==0 and y_pred ==0:
            TN +=1
	
	accuracy = (TP + TN)/(TP + TN + FP + FN) if (TP + TN + FP + FN) != 0 else 0
	precision = TP/(TP + FP) if (TP + FP) != 0 else 0
	recall = TP/(TP + FN) if (TP + FN) != 0 else 0

	f1 = 2*precision*recall/(precision + recall)if (precision + recall) !=0 else 0

	specificity = TN/(TN + FP)if (TN + FP) != 0 else 0
	negativePredictive = TN/(TN + FN)if (TN + FN) != 0 else 0

	confusion_matrix = [
        [TP, FN],
        [FP, TN]
    ]

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

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
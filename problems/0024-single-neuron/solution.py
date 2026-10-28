import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	X = np.array(features)
	w = np.array(weights)
	y = np.array(labels)
	
	z = X @ w + bias
	prob =1 / (1 + np.exp(-z))
	mse = np.mean((prob - y) ** 2)

	prob_rounded = [round(p, 4) for p in prob.tolist()]	
    mse_rounded = round(mse, 4)
    
    return prob_rounded, mse_rounded
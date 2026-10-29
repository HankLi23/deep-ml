import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	# padding
	paded = np.pad(input_matrix, pad_width = padding, mode = "constant", constant_values = 0)
    paded_h, paded_w = paded.shape

	# output
	out_h = (paded_h - kernel_height)//stride + 1
	out_w = (paded_w - kernel_width)//stride + 1
	output_matrix = np.zeros((out_h, out_w))

	# convolution
	for i in range(out_h):
		for j in range(out_w):
			y_start = i * stride
			y_end = y_start + kernel_height
			x_start = j * stride
			x_end = x_start + kernel_width

			windows = paded[y_start:y_end, x_start:x_end]
			output_matrix[i, j] = np.sum(windows * kernel)


	return output_matrix

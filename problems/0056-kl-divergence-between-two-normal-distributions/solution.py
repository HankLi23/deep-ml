import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	if sigma_p == 0 or sigma_q == 0: return 0.0
	
	term1 = np.log(sigma_q / sigma_p)
	term2 = (sigma_p ** 2 + (mu_p - mu_q) ** 2)/(2 * sigma_q ** 2)

	return term1 + term2 -1/2
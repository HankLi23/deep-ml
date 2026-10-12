import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    # Note: `f` is accepted only for interface parity with the PyTorch/Tinygrad
    # variants, which derive gradients from it via autograd. This version uses
    # `grad` only — the objective value `f` is never evaluated.
    # Your code here
    x = np.copy(x0)
    mt = np.zeros_like(x)  
    vt = np.zeros_like(x) 

    for t in range(1, num_iterations + 1):
        g = grad(x)
        mt = beta1 * mt + (1-beta1) * g
        vt = beta2 * vt + (1-beta2) * (g ** 2)
        
        mt_pred = mt/(1 - beta1 ** t)
        vt_pred = vt/(1-beta2 ** t)

        x = x - learning_rate*mt_pred/(np.sqrt(vt_pred) + epsilon) 
    
    return x
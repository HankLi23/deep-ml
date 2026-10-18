import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    idx = np.arange(n_samples)

    if shuffle:
        np.random.shuffle(idx)

    folds = []
    start = 0
    fold_size, reminder = divmod(n_samples, k)

    for i in range(k):
        if i == 0:
            current_size = fold_size + reminder 
        else:
            current_size = fold_size
        end = start + current_size
        fold = idx[start:end]
        folds.append(fold)
        start = end
    
    result = []
    for test_fold in folds:
        train_folds = []
        for f in folds:
            if f is not test_fold:
                train_folds.extend(f)
        result.append((train_folds, test_fold))
    
    return result
    

    
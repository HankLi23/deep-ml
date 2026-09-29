import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    arr = np.asarray(data)
    
    mean = np.mean(arr)
    median = np.median(arr)

    values, counts = np.unique(arr, return_counts=True)
    mode_val = values[np.argmax(counts)]
    
    # Population variance (ddof=0 -> divide by N)
    variance = np.var(arr, ddof=0)
    standard_deviation = np.std(arr, ddof=0)
    
    p25 = np.percentile(arr, 25)
    p50 = np.percentile(arr, 50)
    p75 = np.percentile(arr, 75)
    iqr = p75 - p25
    
    result = {
        "mean": mean,
        "median": median,
        "mode": mode_val,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr
    }
    return result
import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    exps = [math.exp(s - max_score) for s in scores]
    sum_exps = sum(exps)
    result = [e / sum_exps for e in exps]
    return result
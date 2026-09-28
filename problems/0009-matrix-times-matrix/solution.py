def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if not a:
        return -1
    if not b:
        return -1
    
    row1 = len(a)
    column1 = len(a[0])

    row2 = len(b)
    column2 = len(b[0])

    if row2 != column1:
        return -1

    result = []
    for k in range(row1):  # 结果有几行
        result_row = []
        for i in range(column2): # 结果有几列
            add = 0
            for j in range(column1):
                add += a[k][j]*b[j][i] 
            result_row.append(add)
        result.append(result_row)
    
    return result
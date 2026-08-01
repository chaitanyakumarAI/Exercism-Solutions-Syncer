def tick(matrix):
    if matrix==[]:
        return matrix
    n=len(matrix)
    m=len(matrix[0])
    old_matrix = [row[:] for row in matrix]
    for i in range(0,n):
        for j in range(0,m):
            row_start = max(0, i - 1)
            row_end = min(n, i + 2)   # min ensures we don't go past the last row
            
            col_start = max(0, j - 1)
            col_end = min(m, j + 2)   # min ensures we don't go past the last column
            
            # 4. Sum up values from our UNCHANGED old_matrix snapshot
            ts = sum(old_matrix[k][l] for k in range(row_start, row_end) 
                                      for l in range(col_start, col_end)) - old_matrix[i][j]
            
            # 5. Apply the rules and write the results into the original matrix
            if (old_matrix[i][j] == 1 and (ts == 2 or ts == 3)) or (old_matrix[i][j] == 0 and ts == 3):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix
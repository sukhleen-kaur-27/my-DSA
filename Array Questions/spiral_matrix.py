from typing import *

def spiralMatrix(matrix : List[List[int]]) -> List[int]:
    #Write your code here.
    n = len(matrix)-1 #4
    m = len(matrix[0])-1 #2
    start_n = 0
    start_m = 0
    temp = []
    while(start_n<=n and start_m<=m):
        for i in range(start_m, m+1):
            temp.append(matrix[start_n][i])
        start_n += 1
        for i in range(start_n, n+1):
            temp.append(matrix[i][m])
        m -= 1
        if(start_n<=n):
            for i in range(m, start_m-1, -1):
                temp.append(matrix[n][i])
            n-=1
        if(start_m<=m):
            for i in range(n, start_n-1,-1):
                temp.append(matrix[i][start_m])
            start_m += 1
    return temp
def zeroMatrix(matrix, n, m):
    # Write your code here.
    i_arr = n*[1]
    j_arr = m*[1]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                i_arr[i]=0
                j_arr[j]=0
    
    if i_arr[0] == 0 :
        for j in range(m):
            matrix[0][j]=0
    elif j_arr[0]==0:
        for i in range(n):
            matrix[i][0]=0

    for i in range(0,n):
        for j in range(0,m):
            if(i_arr[i]==0 or j_arr[j]==0):
                matrix[i][j]=0
    return matrix
    
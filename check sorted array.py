def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if(a[j]<a[j-1]):
    #             return 0
    # return 1
    for i in range(1,n):
        if(a[i]<a[i-1]):
            return 0
    return 1
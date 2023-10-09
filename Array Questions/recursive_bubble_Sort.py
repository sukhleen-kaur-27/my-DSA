from typing import List
def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    # for i in range(n):
    #     for j in range(1,n-i):
    #         if (arr[j-1]>arr[j]):
    #             (arr[j-1], arr[j]) = (arr[j], arr[j-1])

    if (n==1):
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    bubbleSort(arr, n-1)
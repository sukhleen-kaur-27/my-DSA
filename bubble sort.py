from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(n):
        for j in range(1,n-i):
            if (arr[j-1]>arr[j]):
                (arr[j-1], arr[j]) = (arr[j], arr[j-1])
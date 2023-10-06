from typing import List
import sys
def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    size=len(arr)
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,size):
            if (arr[j]<arr[min_index]):
                min_index=j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
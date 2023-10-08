from typing import List
def partition(arr :List[int], startIndex: int, endIndex: int):
    pivot = arr[startIndex]
    i = startIndex
    j = endIndex
    while (i<j):
        while (arr[i]<=pivot and i<=endIndex-1):
            i+=1
        while(arr[j]>pivot and j>=startIndex+1):
            j-=1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[startIndex] = arr[startIndex], arr[j]
    return j
        
def quickSort(arr: List[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if (startIndex<endIndex):      
        pivot = partition(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pivot-1)
        quickSort(arr, pivot+1, endIndex)
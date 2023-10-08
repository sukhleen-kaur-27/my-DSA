from typing import *

def nextGreaterPermutation(arr : List[int]) -> List[int]:
    # Write your code here.
    breakpoint = -1
    n = len(arr)
    for i in range(n-1, 0, -1):
        if(arr[i]>arr[i-1]):
            breakpoint=i-1
            break
    if breakpoint==-1:
        return reversed(arr)
    for i in range(n-1, -1, -1):
        if(arr[breakpoint]<arr[i]):
            arr[breakpoint], arr[i] = arr[i], arr[breakpoint]
            break
    arr[breakpoint+1:] = reversed(arr[breakpoint+1:])
    return arr
    
from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    a.sort()
    maxi = 1
    maxval = 0
    for i in range(len(a)-1):
        if a[i+1]-a[i]==1:
            maxi+=1
        elif (a[i]!=a[i+1]) :
            maxi =1
        maxval = max(maxi, maxval)
    return maxval
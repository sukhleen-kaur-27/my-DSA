from os import *
from sys import *
from collections import *
from math import *

def ceilingInSortedArray(n, x, arr):
    # Write your code here.
    low = 0
    high = n-1
    ceil_val = -1
    floor_val = -1
    while(low<=high):
        mid = (low+high)//2
        if (arr[mid]>=x):
            high = mid-1
            ceil_val = arr[mid]
        else: 
            low = mid+1
            
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<=x):
            low = mid+1
            floor_val = arr[mid]
        else:
            high = mid-1
            
    return str(floor_val)+ " " +  str(ceil_val)

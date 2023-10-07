from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    max_val = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            max_val = max(max_val, sum)
    # return the answer
    return max_val

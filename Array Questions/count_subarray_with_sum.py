from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    # count=0
    # n = len(arr)
    # for i in range(n):
    #     sum = 0
    #     for j in range(i,n):
    #         sum+=arr[j]
    #         if (sum==s):
    #             count+=1
    # return count
    mpp = defaultdict(int)
    n = len(arr)
    prefix_sum = 0
    count = 0
    mpp[0] = 1
    for i in range(n):
        prefix_sum+=arr[i]
        if (prefix_sum-s) in mpp:
            count += mpp[prefix_sum-s]
        mpp[prefix_sum]+=1
    return count
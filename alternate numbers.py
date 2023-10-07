from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    temp = len(a) * [0]
    ind_pos = 0
    ind_neg = 1
    for i in range(len(a)):
        if a[i]>0:
            temp[ind_pos]=a[i]
            ind_pos+=2
        else:
            temp[ind_neg]=a[i]
            ind_neg+=2
    return temp
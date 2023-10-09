from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    superior = [a[-1]]
    max = a[-1]
    for i in range(len(a)-2, -1,-1):
        if a[i]>max:
            superior.append(a[i])
            max = a[i]
    return superior
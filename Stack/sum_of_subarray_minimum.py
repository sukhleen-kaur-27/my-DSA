from typing import *
def NSL(arr,n):
    stack = []
    small = []
    for i in range(n):
        while (stack and arr[stack[-1]]>=arr[i]):
            stack.pop()
        if stack:
            small.append(stack[-1])
        else:
            small.append(-1)
        stack.append(i)
    return small


def NSR(arr, n):
    stack = []
    small = []
    for i in range(n-1, -1,-1):
        while(stack and arr[stack[-1]]>arr[i]):
            stack.pop()
        if stack:
            small.append(stack[-1])
        else:
            small.append(n)
        stack.append(i)
    return small[::-1]

def sumSubarrayMins(N:int, arr:List[int]) -> int:
    # Write your code here
    nsl = NSL(arr, N)
    nsr = NSR(arr, N)
    sum = 0
    for i in range(N):
        l = i - nsl[i]
        r = nsr[i] - i
        total = l*r
        sum = sum + (total*arr[i])
    return sum % (10**9 +7)


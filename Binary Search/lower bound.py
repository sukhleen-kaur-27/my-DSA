def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low = 0
    high = n-1
    ans = n
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]<x:
            low = mid+1
        else:
            ans = mid
            high = mid-1
    return ans
        
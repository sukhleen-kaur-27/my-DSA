def findMin(arr: [int]):
    # Write your code here.
    n = len(arr)
    low = 0
    high = n-1
    minVal = float("inf")
    while(low<=high):
        mid = (low+high)//2
        if(arr[low]<=arr[mid]):
            minVal = min(minVal, arr[low])
            low = mid+1
        else:
            minVal = min(minVal, arr[mid])
            high = mid-1
    return minVal
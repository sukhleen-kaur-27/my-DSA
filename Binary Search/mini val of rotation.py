def findKRotation(arr : [int]) -> int:
    # Write your code here.
    low = 0
    high = len(arr)-1
    minVal = -1
    ans = float("inf")
    while(low<=high):
        mid = (low+high)//2
        if(arr[low]<=arr[high]):
            if(arr[low]<ans):
                minVal = low
                ans = arr[low]
            break
        if(arr[low]<=arr[mid]):
            if(arr[low]<ans):
                minVal = low
                ans = arr[low]
            low = mid+1
        else:
            if(arr[mid]<ans):
                minVal = mid
                ans = arr[mid]
            high = mid-1
    return minVal
def firstAndLastPosition(arr, n, k):
    # Write your code here
    low = 0
    high = n-1
    first = -1
    last = -1
    while(low<=high):
        mid = (low+high)//2
        if (arr[mid]>=k):
            if(arr[mid]==k):
                first = mid
            high = mid-1
        else:
            low = mid+1
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<=k):
            if(arr[mid]==k):
                last = mid
            low = mid+1
        else:
            high = mid-1

    return first, last
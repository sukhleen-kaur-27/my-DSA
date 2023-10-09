def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    low = 0
    high = n-1
    first = -1
    last = -1
    #finding first
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]>=x):
            if(arr[mid]==x):
                first = mid
            high = mid-1
        else:
            low = mid+1
    # print(first)
    #finding last 
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<=x):
            if(arr[mid]==x):
                last = mid
            low = mid+1
        else: 
            high = mid-1
    # print(last)
    if(last==-1 and first==-1):
        return 0
    return (last-first+1)
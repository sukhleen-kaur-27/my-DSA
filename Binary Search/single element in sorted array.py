def singleNonDuplicate(arr):
    # Write your code here
    low = 0
    high = len(arr)-1
    if (len(arr)==1):
        return arr[0]
    if(arr[low]!=arr[low+1]):
        return arr[low]
    if(arr[high]!=arr[high-1]):
        return arr[high]
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid-1]!=arr[mid] and arr[mid]!=arr[mid+1]):
            return arr[mid]
        if((mid%2==1 and arr[mid]==arr[mid-1])  or(mid%2==0 and arr[mid+1]==arr[mid])):
            low = mid+1
        else:
            high = mid-1
    return -1
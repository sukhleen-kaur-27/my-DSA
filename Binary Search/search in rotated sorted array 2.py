from typing import *

def searchInARotatedSortedArrayII(arr : List[int], key : int) -> bool:
    # Write your code here.
    low=0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==key):
            return True
        if(arr[mid]==arr[low] and arr[mid]==arr[high]):
            low+=1
            high-=1
            continue
        if(arr[low]<=arr[mid]):
            if(arr[low]<=key and key<=arr[mid]):
                high = mid-1
            else:
                low = mid+1
        else:
            if(arr[mid]<=key and key<=arr[high]):
                low=mid+1
            else:
                high = mid-1
    return False
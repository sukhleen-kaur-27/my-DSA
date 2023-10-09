def binarySearch(arr: [int], target: int, low: int, high: int):
    if(low>high):
        return -1
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binarySearch(arr, target, mid+1, high)
    return binarySearch(arr, target, low, mid-1)
    


def search(nums: [int], target: int):
    # write your code logic !!
    return binarySearch(nums, target, 0, len(nums)-1)

print(search( [1, 3, 7, 9, 11, 12, 45], 3))
print(search( [1, 2, 3, 4, 5, 6, 7], 9))
print(search( [5, 9, 14, 15, 16, 22, 23, 24, 28, 29, 34 ], 16))

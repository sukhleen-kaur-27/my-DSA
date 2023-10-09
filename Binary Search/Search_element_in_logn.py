from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr: [int], target: int, low: int, high: int):
            if(low>high):
                return -1
            mid = (low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                return binarySearch(arr, target, mid+1, high)
            else:
                return binarySearch(arr, target, low, mid-1)
        return binarySearch(nums, target, 0, len(nums)-1)

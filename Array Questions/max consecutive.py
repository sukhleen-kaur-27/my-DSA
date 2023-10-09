def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    i = 0
    j = 0
    maxval = 0
    for k in range(len(nums)):
        if (nums[k]==1):
            if(k!=0 and nums[k-1]!=1):
                i=k
            j=k
            maxval = max(j-i+1, maxval)
    return maxval
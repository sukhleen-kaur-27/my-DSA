def singleNumber(self, nums: List[int]) -> int:
    temp ={}
    for i in range(len(nums)):
        if(nums[i] not in temp):
            temp[nums[i]] = 1
        else:
            temp[nums[i]] = temp[nums[i]]+1
    for i,j in temp.items():
        if j==1:
            return i
    return -1